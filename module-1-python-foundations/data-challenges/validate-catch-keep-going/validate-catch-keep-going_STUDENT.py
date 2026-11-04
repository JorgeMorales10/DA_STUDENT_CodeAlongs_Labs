#!/usr/bin/env python3
"""Validate, Catch, Keep Going: see DataChallengeOverview&Steps.md."""

DATA_FILE = "../data/service_requests.csv"  # edit the filepath with the data

with open(DATA_FILE) as f:
    lines = f.read().splitlines()

header = lines[0]
rows = [line for line in lines[1:] if line]


# ===== Day 1 =====

# Step 1: Write `validate_request()` to Return a Verdict and a Reason
EXPECTED_FIELDS = 5
ALLOWED_STATUS = ["Open", "In Progress", "Closed"]
# TODO: assign `EXPECTED_FIELDS` to 5
# TODO: assign `ALLOWED_STATUS` to ["Open", "In Progress", "Closed"]


def validate_request(row):
    # TODO: assign `fields` to `row` split on commas
    fields = row.split(",")
    if len(fields) != EXPECTED_FIELDS:
        return False, "wrong field count: " + str(len(fields))
    request_id, complaint_type, borough, days_open, status = fields
    if borough == (""):
        return False, "borough is empty" 
    elif not status in ALLOWED_STATUS:
        return False, "status not allowed: " + status
    else: 
        return True, "ok"
    
    # TODO: unpack `fields` into the five names in the CSV header
    # TODO: if `borough` is empty, return False and "borough is empty"
    # TODO: if `status` is not in ALLOWED_STATUS, return False and a reason
    # TODO: make that reason "status not allowed: " plus `status`
    # TODO: return True and "ok"
    pass


print(validate_request("SR-1001,Noise - Residential,Brooklyn,3,Closed"))
print(validate_request("SR-1004,Rodent,,6,Closed"))
print(validate_request("SR-1009,Water System,Queens,4,Escalated"))

# Step 1, answer 1:
#One row holds request_id, complaint_type, borough, days_open, status, the problem with 
#this is that the complaint_type are together which makes it harder reading it when it has 
#two types of data which is complaints and the type of place it takes up with.
# Step 1, answer 2:
#The caller take the two returned apart of one line by acting like a tuple with a boolean value
#and a string value.


# Step 2: Run All 15 Rows Through the Validator and Report Each Rejection
valid = 0
for row in rows:
    ok, reason = validate_request(row)
    if ok:
        valid += 1
    else:
        print(row.split(",")[0], "Rejected -", reason)


# TODO: assign `valid` to 0
# TODO: loop over `rows`; unpack validate_request(row) into ok, reason
# TODO: if `ok`, add 1 to `valid`
# TODO: else print row.split(",")[0], "REJECTED -" and `reason`

print("header:", header)
print("rows read:", len(rows))
print("passed Day 1 validation:", valid)

# Step 2, answer 1:
#The amount of rows that fail the three rules is 3, each rule looks for boroughs not being
#empty and status not being allowed because it has 3 distinct strings to define status.
# Step 2, answer 2:
#The one that got through that shouldn't have was SR-1014 they missed the days_open being
#-3, the reason the validator did not see them was because they were looking for borough and 
#status, not the days_open or the other rows.


# ===== Day 2 =====

# Step 3: Build the Days-Open Report With No Protection and Watch It Crash
total_days = 0
counted = 0
#for row in rows:
#    ok, reason = validate_request(row)
#    if not ok:
#        continue
#    x = row.split(",")
#    days_open = int(x[3])
#    total_days += days_open 
#    counted += 1
#    print(x[0], "Days open:", days_open)
    

# TODO: assign `total_days` and `counted` to 0
# TODO: loop over `rows`; `continue` past any row validate_request() rejects
# TODO: assign `days_open` to int() of the row's fourth field
# TODO: add `days_open` to `total_days` and 1 to `counted`
# TODO: print the row's ID, "days open:" and `days_open`
# TODO: after your answers, comment out this step so Step 4 can run

#print("average days open:", total_days / counted)

# Step 3, answer 1:
#I predict that it would run till the request_id is SR-1007 because it's not a whole number
#instead it says "3 days" which is not the same as "3" itself.
# Step 3, answer 2:
#    days_open = int(x[3])
#ValueError: invalid literal for int() with base 10: '3 days'
#at least 6 rows were printed out.
# Step 3, answer 3:
#The rows the loop never reaches doesn't ever get printed or read.


# Step 4: Rebuild the Report So Every Row Is Counted or Skipped
def check_days_open(value):
    try:
        days = int(value)
    except ValueError:
        return False, "days_open is not a number:" + value
    if days < 0:
        return False, "days_open is negative:" + value
    return True, "ok"
    # TODO: in a try, assign `days` to int(value)
    # TODO: in except ValueError, return False and a reason
    # TODO: make that reason "days_open is not a number: " plus `value`
    # TODO: if `days` is below 0, return False and a reason
    # TODO: make that reason "days_open is negative: " plus `value`
    # TODO: return True and "ok"
    pass

total_days = 0
counted = 0
skipped = 0
for row in rows:
    ok, reason = validate_request(row)
    if ok:
        ok, reason = check_days_open(row.split(",")[3])
    if ok:
        days_value = int(row.split(",")[3])
        total_days += days_value
        counted += 1
    else:
        skipped += 1
        print(row.split(",")[0], "SKIPPED - ", reason)

# TODO: assign `total_days`, `counted` and `skipped` to 0
# TODO: loop over `rows`; unpack validate_request(row) into ok, reason
# TODO: if ok, unpack check_days_open() of the fourth field into ok, reason
# TODO: if still ok, add the days to `total_days` and 1 to `counted`
# TODO: else add 1 to `skipped`; print the ID, "SKIPPED -" and `reason`

print("counted:", counted, "| skipped:", skipped)
print("average days open:", round(total_days / counted, 1))

# Step 4, answer 1:
#At least 5 rows will show that they were skipped and the one my validator let through was the
#SR-1007 which had a "3 days" and SR-1013 which had a negative number.
# Step 4, answer 2:
#I would say if was missing unless you put a certain rule that can find it while try can also go through 
#it all but would stop at a certain point as well.
# Step 4, answer 3:
#Yes they count for each row that follows up with there rule as well as skipped where they both total
#to at least 15 rows.
#counted: 10 | skipped: 5
