#!/usr/bin/env python3
"""Lookups Matter: see DataChallengeOverview&Steps.md for the steps."""

import csv

DATA_FILE = "../data/member_directory.csv"  # edit the filepath with the data
CHECKINS_FILE = "../data/door_checkins.txt"  # edit the filepath with the data

with open(DATA_FILE, newline="") as f:
    members = list(csv.DictReader(f))


# Step 1: Write `find_linear()` to Return the Member and Its Comparisons
def find_linear(members, member_id):
    comparisons = 0
    for row in members:
        comparisons += 1
        if row["member_id"] == member_id:
            return row, comparisons
    return None, comparisons
    # TODO: assign `comparisons` to 0
    # TODO: loop over `members`; add 1 to `comparisons` for every row
    # TODO: inside the loop, return row, comparisons on a member_id match
    # TODO: after the loop, return None, comparisons
    pass


row, count = find_linear(members, "M1150")
print("members in the directory:", len(members))
print("found:", row["name"], "at", row["home_branch"])
print("comparisons:", count)

# Step 1, answer 1:
#My predicted count for M1150 will be at least 150 because it starts off at M1001 and it will count up to 
#M1150 and the output I got was 150 comparisons


# Step 2: Total the Comparisons for All 20 Swipes in `door_checkins.txt`
with open(CHECKINS_FILE) as f:
    swipes = f.read().splitlines()
linear_total = 0
not_members = 0
for member_id in swipes:
    row, comparisons = find_linear(members, member_id)
    linear_total += comparisons
    if row is None:
        not_members += 1
        print(f"{member_id}: NOT A MEMBER({comparisons} comparisons)")
    else:
        print(f"{member_id}: {row['name']} ({comparisons} comparisons)")
    
# TODO: open CHECKINS_FILE in a with block as `f`
# TODO: inside it, assign `swipes` to f.read().splitlines()
# TODO: assign `linear_total` and `not_members` to 0
# TODO: loop over `swipes`; call find_linear(members, member_id)
# TODO: print the ID, the name or "NOT A MEMBER", and the comparisons
# TODO: add each count to `linear_total`
# TODO: add 1 to `not_members` for every swipe with no row

print("swipes:", len(swipes), "| not members:", not_members)
print("linear total comparisons:", linear_total)

# Step 2, answer 1:
#My predictions for the cost of each of the first 3 swipes is M1004, M1012, M1027 which would sum up to 43 and 
#the cost of the non members swipe would be 312 comparisons because from the data it shows M1313 which would lead
#me to think that from that point to M1001 would be costly.
# Step 2, answer 2:
#I would say the swipes that cost the most would 312 coming from M1313 and M2041. This is because they are not members
#which would make it look through every line of the data costing it more.


# Step 3: Build `members_by_id` and Find the Swipe Where It Pays Off
members_by_id = {}
build_steps = 0
for row in members:
    members_by_id[row["member_id"]] = row
    build_steps += 1

def find_dict(members_by_id, member_id):
    return members_by_id.get(member_id), 1

# TODO: assign `members_by_id` to an empty dict and `build_steps` to 0
# TODO: loop over `members`; store each row under row["member_id"]
# TODO: add 1 to `build_steps` for every row
# TODO: write find_dict(members_by_id, member_id)
# TODO: make find_dict() return members_by_id.get(member_id), 1

print("build cost:", build_steps, "| keys in the dict:", len(members_by_id))

# TODO: assign `linear_running` to 0 and `dict_running` to build_steps
# TODO: assign `pays_off_at` to None and `swipe_number` to 0
linear_running = 0
dict_running = build_steps
pays_off_at = None
swipe_number = 0
for member_id in swipes:
    swipe_number += 1
    # TODO: add 1 to `swipe_number`
    _, linear_count = find_linear(members, member_id)
    _, dict_count = find_dict(members_by_id, member_id)

    linear_running += linear_count
    dict_running += dict_count
    print(swipe_number, member_id, linear_running, dict_running)

    if pays_off_at is None and dict_running < linear_running:
        pays_off_at = swipe_number
    # TODO: add each search's count to its running total
    # TODO: print swipe_number, the ID and both running totals
    # TODO: the first time dict_running < linear_running, set `pays_off_at`

print("dict pays off at swipe:", pays_off_at)
print("morning totals | linear:", linear_running, "| dict:", dict_running)

# Step 3, answer 1:
#The swipe the dict total first drop below the linear total is at the swipe of 6 because its not a member which 
#would take more to look for it.
# Step 3, answer 2:
#A dictionary keyed on member_id fits the door's job because it can track each unique card of each members 
#when going through the door even for non members.6 M1313 574 318 this quote from the output shows the amount 
#it takes to look for the non member here and looked throughout all the dict to find it.
# Step 3, answer 3:
#For a list to be a better choice in the morning would need to be at least an average of 2 swipes so it wouldn't
#be too costly and they could use last names or a different way to search through a specific person or member.


# Step 4: Test an AI Speed Claim Against Your Totals and Write a Verdict
# TODO: replace the text below with your AI's claim, word for word
ai_claim = "For 20 lookups in a list of 312 rows, a dictionary lookup is about 9.4 times faster overall " \
"(including the upfront cost of building the dictionary) and 156.5 times faster when comparing the lookup " \
"steps alone on average."
print("AI CLAIM:", ai_claim)
_, front_count = find_linear(members, swipes[0])
_, absent_count = find_linear(members, "M1313")
ratio = round(linear_running / dict_running, 1)

# TODO: unpack find_linear() for swipes[0] into `_, front_count`
# TODO: unpack find_linear() for "M1313" into `_, absent_count`
# TODO: assign `ratio` to round(linear_running / dict_running, 1)

print("one front-of-file swipe | linear:", front_count, "| dict: 1")
print("one non-member swipe | linear:", absent_count, "| dict: 1")
print("whole morning | linear:", linear_running, "| dict:", dict_running,
      "| ratio:", ratio)

# TODO: replace the text below with your own verdict
verdict = "The real speed is 8.8 being shown on the ratio from the output, much more different from the what AI claimed."
print("VERDICT:", verdict)

# Step 4, answer 1:
#It matched the absent_count of the one non-member swipe, it missed the speed of the dictionary which was 8.8x 
#when the AI claim is 9.4x.
# Step 4, answer 2:
#No, it did not count the cost of the building so it only showed a speed of 9.4x. It said that the reason was
#that it assumed that the member id were randomly placed which gave it the 9.4x speed but when it realize it wasn't
#all random it saw that the ratio was correct and 8.8x speed
