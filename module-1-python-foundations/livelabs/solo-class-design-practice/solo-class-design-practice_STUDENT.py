#!/usr/bin/env python3
"""Lab: Solo Class Design Rep
GitBook Quest 1.8: Meet the Objects

HOW TO RUN
    Open a terminal in this file's folder and run:
        python3 solo-class-design-practice_STUDENT.py
    Or make it executable once:
        chmod +x solo-class-design-practice_STUDENT.py
    and from then on run it directly:
        ./solo-class-design-practice_STUDENT.py
    The first line, #!/usr/bin/env python3 (the "shebang"), is what
    makes ./ work. python3 <file> ignores it as a comment.

ANSWER EVERYTHING IN THIS FILE
    - Code goes under each step's banner.
    - Written answers go in # comments under each "# Your answer:"
      line.
    - Run the file after every change. It runs top to bottom, so a
      later step can use anything an earlier step made.

HINTS live in the worksheet (LiveLabOverview&Steps.md), collapsed
under each step. Open one only when you are stuck.

SUBMIT
    Commit this file (you may rename it solo-class-design-practice.py) to your own data
    challenge repo, inside your Module 1 folder. Paste its direct GitHub URL
    into the LMS.
"""

# ===== Step 1: Read the Stakeholder Need =====
# A new stakeholder need. Not the board-game or office-supply domain from
# lecture, and not one of the project's own 4 scenarios.

# Your answer:
#The stake holder needs the Tool names or identifier, as well as the Tools available and are in use, and 
#they need a safety check or inspection of the tools that are capable.

# ===== Step 2: Decide Your Attributes, Each With a Reason From the Scenario =====

# Your answer:
#    def __init__(self,Tool_name, Date, Available_tools, Tools_in_use, Safety_check):
#        self.Tool_name = This is naming each individual tools and name
#        self.Date = Keeping the track of the date of the tools being used
#        self.Available_tools = Showing the amount of available tools there are
#        self.Tools_in_use = This helps show how many tools are still being used while trying to seek the others
#        self.Safety_check = This is the label that is checking whether they have done inspection or safety check so it could be used or not


# ===== Step 3: Write __init__ and a Method, From Scratch =====
# There is no single correct design here. Your class name, your attribute
# names and your method can all differ from everyone else's and still be
# right. The test is whether each one traces back to the stakeholder
# paragraph.

# TODO: Write __init__ and a Method, From Scratch
import json

DATA_FILE = "Community_sharing_tools.json"

with open(DATA_FILE) as f:
    stations = json.load(f)

class Tools:
    def __init__(self,Tool_name, Date, Available_tools, Tools_in_use, Safety_check):
        self.Tool_name = Tool_name
        self.Date = Date
        self.Available_tools = Available_tools
        self.Tools_in_use = Tools_in_use
        self.Safety_check = Safety_check
    def Availability_check(self):
        if self.Available_tools == 0:
            return "No Available tools at the moment, out of stock."
        else:
            return "Yes, we have some available tools for you."
    def Safety_checked(self):
        if self.Safety_check == True:
            return "We checked and clear."
        else:
            return "No hasn't been checked."
    def __str__(self):
        return f"(Tools{self.Tool_name}: {self.Safety_check()}, {self.Availability_check()})"
# ===== Step 4: Instantiate 2+ Objects, Confirm Independent Storage =====
# The same proof Day 13's lecture asked for, now on a class you designed
# yourself. Predict what each print() will show before you run it.
drills = Tools("drills","Nov 11th", 5, 2, True)
ladders = Tools("ladders","Nov 11th", 3, 1, False)
saws = Tools("saws", "Nov 11th", 2, 0, False)
hammers = Tools("hammers", "Nov 11th", 0, 7, True)

print(drills.Availability_check())
#predictions = Yes, we have some available tools for you.
#output = Yes, we have some available tools for you.
print(ladders.Availability_check())
#predictions = Yes, we have some available tools for you.
#output = Yes, we have some available tools for you.
print(saws.Availability_check())
#predictions = Yes, we have some available tools for you.
#output = Yes, we have some available tools for you.
print(hammers.Availability_check())
#predictions = No Available tools at the moment, out of stock.
#output = No Available tools a the moment, out of stock.
# TODO: Instantiate 2+ Objects, Confirm Independent Storage
print(drills.Safety_check)
#predict =True
#output=True
print(ladders.Safety_check)
#predict = False
#output = False
print(saws.Safety_check)
#predict =False
#output = False
print(hammers.Safety_check)
#predict = True
#output = True 
# ===== Step 5: Justify Your Design Choice in 2-3 Sentences =====

# Your answer:
#The reason I chose this design was because it was the most recent work we've been doing and I like using dictionary to 
#help create a more neater and easier design. I felt more confident in building it up with import json and creating a class,
#method,objects and attributes. It felt like a better way to find and look for an issue and specific way to find each commands made.

# ----- Share Out -----
# Last 15 minutes, back together as a class. Bring:
#
# Come ready to show your class and defend it. Specifically:
# - The attribute list you chose, and for each one, the phrase in the
#   coordinator's request it came from. If you can't point at a phrase for
#   an attribute, say so - that's a real finding, not a failure.
# - One attribute you considered and rejected, and why. - Your method: what
#   question does it answer, and why would the coordinator reach for it
#   first?
# - Anything you got stuck on. Designing from a paragraph with nobody to
#   check against is genuinely hard, and naming where it was hard is worth
#   more to the room than a tidy answer.
#
# Expect to be asked "why that attribute and not another?" - there is no
# single right list here, so the reasoning IS the answer.
#
# Be ready to answer "why did you do it that way?"

# Your notes for the share out:
#They were also using json but they were adding more attributes and labeling was different a bit.
#I was changing my objects and its attributes because it was getting more difficult for me to continue 
#it and made it simpler with less and trying to understand each part better.
