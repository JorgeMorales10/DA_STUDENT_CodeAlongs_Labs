#!/usr/bin/env python3
"""One Job at a Time: see DataChallengeOverview&Steps.md for the steps."""

import json

DATA_FILE = "../data/pantry_donations.csv"  # edit the filepath with the data


# ===== Day 1 =====

# Step 1: Write the Read-and-Validate Pair, Each With a Docstring
def read_donations(path):
    """Read the donation log into one raw string per record."""
    records = []
    with open(path) as f:
        for line in f.read().splitlines()[1:]:
            if line.strip():
                records.append(line)
    return records


def validate_donation(record):
    """"Returns a verdict and a reason for one record"""
    parts = record.split(",")
    if len(parts) != 5:
        return False, ("wrong field count")
    if parts[2].strip() == "":
        return False, ("missing category")
    try:
         float(parts[3])
    except ValueError:
        return (False, "pounds is not a number")
    return (True, "")

    # TODO: add a one-sentence docstring naming its one job
    # TODO: assign `parts` to `record` split on commas
    # TODO: return False, "wrong field count" if `parts` lacks 5 fields
    # TODO: return False, "missing category" if parts[2].strip() is ""
    # TODO: in a try, call float(parts[3])
    # TODO: in except ValueError, return False, "pounds is not a number"
    # TODO: return True and ""
    pass

records = read_donations(DATA_FILE)
valid = []
for record in records:
    ok, reason = validate_donation(record)
    if ok:
        valid.append(record)
    else:
        print("rejected", record.split(",")[0] + ":", reason)
# TODO: assign `records` to read_donations(DATA_FILE), `valid` to []
# TODO: loop over `records`; unpack validate_donation(record) as ok, reason
# TODO: if `ok`, append `record` to `valid`
# TODO: else print "rejected", the record's ID plus ":", and `reason`
print(len(valid), "usable records out of", len(records))

# Step 1, answer 1:
#On record it will hold at least 17 wil be usable out of 20, and the 9th donation_id was already wrong
#its missing a category and 17 as well missing pounds but its the date in pounds category.
# Step 1, answer 2:
#The three things my validator promises about each record 


# Step 2: Write `summarize_donations()` for the Category Breakdown Only
def summarize_donations(valid_records):
    """"One loop and one dict that totals pounds per category"""
    by_category = {}
    total_pounds = 0.0
    for record in valid_records:
        parts = record.split(",")
        category = parts[2]
        pounds = float(parts[3])
        if not category in by_category :
            by_category[category] = {"donations": 0, "pounds": 0.0}
        by_category[category]["donations"] += 1
        by_category[category]["pounds"] += pounds
        total_pounds += pounds

    return{"records": len(valid_records), "total_pounds": total_pounds, "by_category": by_category}
    # TODO: add a one-sentence docstring naming its one job
    # TODO: assign `by_category` to {} and `total_pounds` to 0.0
    # TODO: loop over `valid_records`; split each record on commas into `parts`
    # TODO: assign `category` to parts[2], `pounds` to float(parts[3])
    # TODO: if `category` is not in `by_category`, add an entry for it
    # TODO: start that entry as {"donations": 0, "pounds": 0.0}
    # TODO: add 1 to its "donations" and `pounds` to its "pounds"
    # TODO: add `pounds` to `total_pounds`
    # TODO: return a dict of "records", "total_pounds" and "by_category"
    pass


# TODO: assign `summary` to summarize_donations(valid)
summary = summarize_donations(valid)
print("records:", summary["records"], "| total pounds:",
      summary["total_pounds"])
for category, stats in summary["by_category"].items():
    print(category, stats["donations"], "donations,", stats["pounds"],
          "lbs")

# Step 2, answer 1:
#I chose protein and I counted 15.0 lbs in total for that category, and when I checked the output
#and its the same.


# ===== Day 2 =====

# Step 3: Add `export_summary()` and `run_pipeline()`, Then Print Docstrings
def export_summary(summary, path):
    """Export_Summary that write a summary to a JSON file """
    with open(path, "w") as f:
        json.dump(summary, f, indent=2)
        return path
    # TODO: add a one-sentence docstring naming its one job
    # TODO: in a with open(path, "w") block, json.dump `summary`, indent=2
    # TODO: return `path`
    pass


def run_pipeline(in_path, out_path, summarize):
    """Run_Pipeline that calls the others in order, the summarizer is one of its parameters"""
    kept = []
    for read in read_donations(in_path):
        ok, reason = validate_donation(read)
        if ok:
            kept.append(read)
    return export_summary(summarize(kept), out_path)
    
    # TODO: add a one-sentence docstring naming its one job
    # TODO: assign `kept` to [] and loop over read_donations(in_path)
    # TODO: append each record that validate_donation() passes to `kept`
    # TODO: return export_summary() of summarize(kept) and `out_path`
    pass


written = run_pipeline(DATA_FILE, "donation_summary.json",
                       summarize_donations)
print("wrote", written)
for func in [read_donations, validate_donation, summarize_donations,
             export_summary]:
    print(func.__name__ + ":", func.__doc__.splitlines()[0])

# Step 3, answer 1:
#Print(len) prints the function reference object (<built-in function len>), whereas 
#print(len("abc")) calls the function with parentheses and returns the integer 3
# Step 3, answer 2:
#No I dont think we need to add and twice and my partner agreed



# Step 4: Swap In `summarize_by_day()` and Count the Functions You Edited
"""Summarize_by_day, that you swap in"""
def summarize_by_day(valid_records):
    by_day = {}
    total_pounds = 0.0
    for record in valid_records:
         parts = record.split(",")
         days = parts[4]
         pounds = float(parts[3])
         if not days in by_day :
            by_day[days] = {"donations": 0, "pounds": 0.0}
         by_day[days]["donations"] += 1
         by_day[days]["pounds"] += pounds
         total_pounds += pounds
    
    return{"records": len(valid_records), "total_pounds": total_pounds, "by_day": by_day}
    # TODO: add a one-sentence docstring naming its one job
    # TODO: return the same dict shape, with "by_day" keyed by parts[4]
    pass


# TODO: call run_pipeline(DATA_FILE, "donation_summary.json", summarize_by_day)
# TODO: replace None with json.load() of "donation_summary.json"
run_pipeline(DATA_FILE, "donation_summary.json", summarize_by_day)
with open("donation_summary.json", "r")as f:
    reloaded = json.load(f)

print("records:", reloaded["records"], "| total pounds:",
      reloaded["total_pounds"])
for day, stats in sorted(reloaded["by_day"].items()):
    print(day, stats["donations"], "donations,", stats["pounds"], "lbs")

# Step 4, answer 1:
#I edited at least 11 functions when I was doing the swap, the summarizer was reaching into 
# Step 4, answer 2:
#
