#!/usr/bin/env python3
"""Looks Right. Is It?: see DataChallengeOverview&Steps.md for the steps."""

DATA_FILE = "../data/timesheet_hours.csv"  # edit the filepath with the data

with open(DATA_FILE) as f:
    lines = f.read().splitlines()


# ===== Day 1 =====

# Step 1: Follow the TypeError in `weekly_hours()` Back to Its Cause
# TODO: run the file as given and read the traceback from the bottom up
# TODO: add print(repr(hours)) as the first line of add_hours(); run again
# TODO: find that printed value in the CSV -- (its printing out days and not the hours)
# TODO: fix the line that reads the wrong column to read the hours column
# TODO: wrap that value in int() so add_hours() adds a number
# TODO: delete the print(repr(hours)) line once Rosa's total is right
def add_hours(total, hours):
    #print(repr(hours))
    return total + hours


def weekly_hours(lines, emp_id):
    total = 0
    for row in lines[1:]:
        parts = row.split(",")
        if parts[0] == emp_id:
            total = add_hours(total, int(parts[3]))
    return total


print("Rosa Alvarez, weekly hours:", weekly_hours(lines, "E101"))

# Step 1, answer 1:
#The total hours Rosa works up to is 40 hours when looking at the csv.
# Step 1, answer 2:
#
# Step 1, answer 3:
#


# Step 2: Trace the ZeroDivisionError Back to the Hand-Typed Staff List
# TODO: run the file as given; note the last ID that printed
# TODO: compare every ID in `staff` with the IDs in the CSV -- (There is an E106 for emp_id that doesn't exist in the csv file.)
# TODO: replace the hand-typed `staff` list with an empty list
# TODO: loop over lines[1:]; append each row's employee ID to `staff` once
# TODO: print "employees in the file:" and len(staff)
def days_worked(lines, emp_id):
    days = 0
    for row in lines[1:]:
        if row.split(",")[0] == emp_id:
            days = days + 1
    return days


staff = []
for row in lines[1:]:
    emp_id = row.split(",")[0]
    if emp_id not in staff:
        staff.append(emp_id)

for emp_id in staff:
    hours = weekly_hours(lines, emp_id)
    days = days_worked(lines, emp_id)
    print(emp_id, "| hours:", hours, "| days:", days,
          "| average per day:", hours / days)
    
print("employees in the file:", len(staff))
# Step 2, answer 1:
#The amount of employees that are in the csv file is at least 5 employees(E101,E102,E103,E104,E105)
# Step 2, answer 2:
#It at least prints out 3 lines before crashing, it stops after the third employer id which was E103
# Step 2, answer 3:
#The bug lives in the list that was created for staff, it shows a emp_id that doesn't exist in the employee
#file so because of a non existed employee its divided 0 to 0 which is creating ZeroDivisionError.


# ===== Day 2 =====

# Step 3: Find Why Four of the Five Weekly Hour Totals Are Wrong
# TODO: add up Rosa's (E101) and Mei's (E103) hours by hand first
# TODO: print("starting", emp, "total is", total) first in the outer loop
# TODO: move the line that sets `total` inside the outer loop
# TODO: delete the "starting" print once all five totals are right
records = []
for row in lines[1:]:
    emp_id, name, day, hours, rate = row.split(",")
    records.append({"id": emp_id, "name": name, "day": day,
                    "hours": int(hours), "rate": float(rate)})

employee_ids = []
for r in records:
    if r["id"] not in employee_ids:
        employee_ids.append(r["id"])

for emp in employee_ids:
    total = 0
    name = ""
    for r in records:
        if r["id"] == emp:
            name = r["name"]
            total = total + r["hours"]
    print(emp, name, "| weekly hours:", total)
print("starting", emp, "total is", total)
# Step 3, answer 1:
#Rosa"s weekly hours is 40 hours and for Mei's weekly hours is 32 hours.
# Step 3, answer 2:
#The total that was held for each employee start was adding on to the one before it, it was adding up from the last total
#of an employee and would start after adding up all the ones the employees had.
# Step 3, answer 3:
#Rosa's number is right because the total is starting by zero so its only adding the first number to zero which hers while
#Priya is getting started with all the rest of the employees total being added up together.


# Step 4: Fix Two Overtime Bugs That Overpay the Firm by $1,810 a Week
# TODO: work out Rosa's, Darnell's and Mei's pay by hand first
# TODO: fix weekly_pay() so it follows the handbook rule word for word
# TODO: fix the other line that compares `total` against 40 the same way
def weekly_pay(hours, rate):
    if hours > 40:
        return (rate * 40) + ((hours - 40) * 1.5)
    return hours * rate


owed_overtime = 0
payroll = 0.0
for emp in employee_ids:
    total = 0
    name = ""
    rate = 0.0
    for r in records:
        if r["id"] == emp:
            name = r["name"]
            rate = r["rate"]
            total = total + r["hours"]
    if total >= 40:
        owed_overtime = owed_overtime + 1
    pay = weekly_pay(total, rate)
    payroll = payroll + pay
    print(f"{name:16} {total:3} hrs  ${pay:>9,.2f}")

print("employees owed overtime:", owed_overtime)
print(f"TOTAL PAYROLL: ${payroll:,.2f}")

# Step 4, answer 1:
#Rosa's weekly pay is (total(40) * rate(24) = $960) 960 dollars, Darnell's weekly pay is (46*31.50=$1,449) 1,449 dollars
#and Mei's weekly pay is (32*28= $896) 896 dollars.
# Step 4, answer 2:
#The two bugs I found were the if loop for hours it was adding more because it wasn't really considering each individual 
#components that were multiplying together when it shouldn't be. So for the rate I multiply with 40 because after 40 hours to
# be overtime and then you would subtract the hours by 40 to get the hours that were overtime then multiplying them with the overtime
#rate which is 1.5 . The second bug was the if loop of "if hours >= 40" which would make any "=" to 40 have to go through the whole
#process.
# Step 4, answer 3:
#The reason Rosa's exact 40 week catch only one bug was because they didn't have overtime but the exact number so it was only catching
#the overtime rate because it was still equal to 40.
