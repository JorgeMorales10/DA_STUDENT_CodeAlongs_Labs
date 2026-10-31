#!/usr/bin/env python3
"""Pick the Right Container: see DataChallengeOverview&Steps.md."""

import json

DATA_FILE = "../data/station_taps.csv"  # edit the filepath with the data

with open(DATA_FILE) as f:
    rows = [line.split(",") for line in f.read().splitlines() if line]

header = rows[0]
taps = rows[1:]


# ===== Day 1 =====

# Step 1: Write `scan_for()` and Count Its Comparisons for Three Tap IDs
def scan_for(tap_id, records):
    comparisons = 0
    for rows in records:
        comparisons += 1
        if rows[0] == tap_id:
            return comparisons
    
    return comparisons

    # TODO: assign `comparisons` to 0
    # TODO: loop over `records`; add 1 to `comparisons` for every row
    # TODO: inside the loop, return `comparisons` when row[0] == tap_id
    # TODO: after the loop, return `comparisons`
    pass


print("columns:", header)
print("rows in the log:", len(taps))
print("comparisons to find T001:", scan_for("T001", taps))
print("comparisons to find T040:", scan_for("T040", taps))
print("comparisons to find T999:", scan_for("T999", taps))

# Step 1, answer 1:
#I predicted that T040, and T999 will be 40 while T001 will be 1 because 
# Step 1, answer 2:
#


# Step 2: Print Scan Cost at 5 to 40 Rows, Then Count a Nested Pair Loop
for size in [5, 10, 20, 40]:
    worst = scan_for("T999", taps[:size])
    print("rows:", size,"| worst-case comparisons:", worst)
pairs = 0
for x in taps:
        for tap in taps:
            pairs += 1

print(len(taps), pairs)
big = len(taps) * 10
print("worst case:", big , "|pair loops:", big * big) 


    # TODO: print "rows:", `size`, "| worst-case comparisons:", `worst`
# TODO: assign `pairs` to 0; loop over `taps` with a loop over `taps` inside
# TODO: add 1 to `pairs` in the inner loop
# TODO: print len(taps) and `pairs`
# TODO: assign `big` to len(taps) * 10
# TODO: print the scan's worst case and the pair loop's count on `big` rows

# Step 2, answer 1:
#
# Step 2, answer 2:
#


# ===== Day 2 =====

# Step 3: Count Taps Per Card With Two Parallel Lists, and Their Comparisons
card_ids = []
tap_counts = []
comparisons = 0
for row in taps:
     card = row[1] 
     found = False
     for i in range(len(card_ids)):
        comparisons += 1
        if card_ids[i] == card:
            tap_counts[i] += 1
            found = True
            break
     if not found:
         card_ids.append(card)
         tap_counts.append(1)

# TODO: assign `card_ids` to an empty list (each card, first-seen order)
# TODO: assign `tap_counts` to an empty list (the count for card_ids[i])
# TODO: assign `comparisons` to 0
# TODO: loop over `taps`; assign `card` to row[1] and `found` to False
# TODO: inside it, loop over range(len(card_ids)); add 1 to `comparisons`
# TODO: if card_ids[i] == card, add 1 to tap_counts[i], set found, break
# TODO: after the inner loop, if not found, append `card` and 1 to the lists

busiest = tap_counts.index(max(tap_counts))
print("distinct cards:", len(card_ids))
print("comparisons the two parallel lists needed:", comparisons)
print("busiest card:", card_ids[busiest], "with", max(tap_counts), "taps")

# Step 3, answer 1:
#
# Step 3, answer 2:
#


# Step 4: Count Taps Per Card With a Dictionary, and Stations With a Set
taps_by_card = {}
lookups = 0
for row in taps:
    lookups += 1
    if row[1] not in taps_by_card:
        taps_by_card[row[1]] = 1
    else:
        taps_by_card[row[1]] += 1
#be aware with using set add the dict to save the information your putting    
stations = set()
for x in taps:
     stations.add(x[2])
#when doing a .add be sure to use the current item in the loop
    
repeat_riders = 0
for i in taps_by_card:
    if taps_by_card[i] > 1:
        repeat_riders += 1
# you need to lookup value stored under the card id key inside your dict
# TODO: assign `taps_by_card` to an empty dict (card ID: tap count)
# TODO: assign `lookups` to 0
# TODO: loop over `taps`; add 1 to `lookups`
# TODO: add 1 to row[1]'s count in `taps_by_card`, or set it to 1 if new
# TODO: assign `stations` to set(); loop over `taps` and .add() row[2]
# TODO: assign `repeat_riders` to 0
# TODO: loop over `taps_by_card`; add 1 to `repeat_riders` if a count is > 1

print("distinct cards:", len(taps_by_card))
print("lookups the dictionary needed:", lookups)
print("unique stations:", len(stations), sorted(stations))
print("cards that tapped more than once:", repeat_riders)
print("taps for C001:", taps_by_card["C001"])

# Step 4, answer 1:
#For look ups it'll probably be 40 cause there are 40 different rows of information
# Step 4, answer 2:
#As the Input Size grows the parallel list will start 
# Step 4, answer 3:
#
# Step 4, answer 4:
#


# ===== Day 3 =====

# Step 5: Save the Summary as JSON and Read the TypeError a Set Causes
# TODO: replace each None with your Day 2 value; keep `stations` a set
summary = {
    "service_day": "2026-03-02",
    "total_taps": len(taps),
    "distinct_cards": len(taps_by_card),
    "stations": (stations),
    "taps_by_card": taps_by_card,
}

print("about to serialize", len(summary), "keys")
# TODO: run the file and answer below before you change anything
# TODO: then put # in front of the next two lines so Step 6 can run
#text = json.dumps(summary, indent=2)
#print(text)

# Step 5, answer 1:
#  File "C:\Users\Jorge Morales\AppData\Local\Python\pythoncore-3.15-64\Lib\json\__init__.py", line 241, in dumps
#    **kw).encode(obj)
##          ~~~~~~^^^^^
#  File "C:\Users\Jorge Morales\AppData\Local\Python\pythoncore-3.15-64\Lib\json\encoder.py", line 202, in encode
#    chunks = self.iterencode(o, _one_shot=True)
#  File "C:\Users\Jorge Morales\AppData\Local\Python\pythoncore-3.15-64\Lib\json\encoder.py", line 263, in iterencode
#    return _iterencode(o, 0)
#  File "C:\Users\Jorge Morales\AppData\Local\Python\pythoncore-3.15-64\Lib\json\encoder.py", line 182, in default
#    raise TypeError(f'Object of type {o.__class__.__name__} '
#                    f'is not JSON serializable')
# Step 5, answer 2:
#
# Step 5, answer 3:
#


# Step 6: Write `tap_summary.json`, Reload It, and Check Which Types Survived
#tap_summary.json
summary["stations"] = sorted(stations)
with open("tap_summary.json", "w")as f:
    json.dump(summary, f)
with open("tap_summary.json", "r")as f:
    reloaded = json.load(f)

# TODO: assign summary["stations"] to a type JSON can hold; keep the key
# TODO: json.dump() `summary` into a with open("tap_summary.json", "w")
# TODO: replace None with json.load() of "tap_summary.json"


print("total_taps came back as:", reloaded["total_taps"])
print("taps_by_card came back as a", type(reloaded["taps_by_card"]).__name__)
print("C001 straight out of the file:", reloaded["taps_by_card"]["C001"])
print("stations came back as a", type(reloaded["stations"]).__name__)
print("round trip identical:", reloaded["taps_by_card"] == taps_by_card)

# Step 6, answer 1:
#
# Step 6, answer 2:
#
