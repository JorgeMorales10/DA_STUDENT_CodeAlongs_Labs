#!/usr/bin/env python3
"""Recall & Practice: Functions, Validation, try/except, Serialization
Module 1: Python Foundations

HOW TO RUN
    Open a terminal in the folder that holds this file (and any data
    file the code reads), then run:
        python3 Module1_Lesson12_recall-practice-functions-validation-try-except-serialization_STUDENT.py
    Or make the file executable once:
        chmod +x Module1_Lesson12_recall-practice-functions-validation-try-except-serialization_STUDENT.py
    and from then on run it directly:
        ./Module1_Lesson12_recall-practice-functions-validation-try-except-serialization_STUDENT.py
    The first line, #!/usr/bin/env python3 (the "shebang"), is what
    makes ./ work: it names the program that runs this file.
    python3 <file> treats that line as a comment and ignores it.

Follow along: type each section as it comes up, then save and run the
file again after each section. Each section prints its own heading,
so you can tell which output belongs to which step.

Complete each TODO as you go. A ____ blank is not valid Python, so
fill it in before you run the file again.
"""

# ===== 1. Any Number of Arguments With *args =====
# Write a total function that adds up any amount of numbers you give it, even
# none at all. * = unpacking operator
print('----- 1. Any Number of Arguments With *args -----')
# TODO: define total(*numbers) that returns sum(numbers)
def total(*numbers):
    return sum(numbers)
#the unpacking is only on the def statement because you only need to unpack it once
print(total(1,2,3))
# TODO: call it with 1, 2, 3 and print the result
print(total(10,20))
# TODO: call it with 10, 20 and print the result
print(total())
# TODO: call it with no arguments at all and print the result
print(total(4,4,4,4))
# PREDICT before you run: What does total(4, 4, 4, 4) return? Write your guess,
#                         then add print(total(4, 4, 4, 4)) under the three
#                         calls in Any Number of Arguments With *args and run
#                         it to check.
# Your answer:
#The output would be 16 adding it all up together
#


# ===== 2. Any Number of Named Arguments With **kwargs =====
# Write describe_game so it prints a game title, then any extra details passed
# in by name.
print('----- 2. Any Number of Named Arguments With **kwargs -----')
# TODO: define describe_game(title, **details) that prints title,
# then loops over details.items() printing "  {key}: {value}"
def describe_game(title, **details):
    print(title)
    for x, y in details.items():
        print(f"{x}: {y}")

# TODO: call it with "Chess", players=2, category="Strategy"
describe_game("Chess", players = 2, category = "Strategy")
# PREDICT before you run: What does describe_game("Uno", players=4) print?
#                         Write your guess, then add that call under the Chess
#                         call in Any Number of Named Arguments With **kwargs
#                         and run it to check.
# Your answer:
#Uno
#players: 4
describe_game("Uno", players = 4)
#if you do a print(type(describe_game("Chess", players = 2, category = "Strategy"))) it will
#print it as a dictionary type because it was not formatted as a dictionary which you would
#need to change and edit.