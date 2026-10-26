#!/usr/bin/env python3
"""Day 4 code-along: Local vs. Global Variables & Scope. Run: python3 <file>"""

# ===== 1. Local Scope, Live =====
# Find out if a variable made inside a function exists outside it.
# TODO: run it, read the NameError, then comment out the raising line
# DISCUSS: Order: A: total disappears. B: make_total() runs. C: total = 100.
# Your answer:
#
print('----- 1. Local Scope, Live -----')
# TODO: define make_total(): set a local total to 100 and return it
# TODO: print total outside the function and see what happens

<<<<<<< HEAD
num_val = 0

def make_total():
    total = 100
    print(total)
    return total * num_val

x = make_total()
print(x)
# DISCUSS: Now try a new function. set_x() runs and sets x = 5 inside it, but
#          print(x) outside raises NameError. Why?
=======
# DISCUSS: set_x() sets x = 5, but print(x) outside raises NameError. Why?
>>>>>>> upstream/main
# Your answer:
#


# ===== 2. Reading a Global, Live =====
# Price a $100 item with 8% tax, using a tax rate stored outside the function.
print('----- 2. Reading a Global, Live -----')
<<<<<<< HEAD
# TODO: define tax_rate as a global, then write
# price_with_tax(price) that reads it without taking it as
# a parameter
tax_rate = .08

def price_with_tax(price):
    x = price + (price * tax_rate)
    return x

print(price_with_tax(11.00))
=======
# TODO: define tax_rate as a global
# TODO: write price_with_tax(price) that reads tax_rate directly
>>>>>>> upstream/main

# DISCUSS: Move price_with_tax to a file with no tax_rate. Why does it break?
# Your answer:
#


# ===== 3. Refactor: Global to Parameter =====
# Pass the tax rate in as a parameter. It should still print 108.0.
print('----- 3. Refactor: Global to Parameter -----')
# TODO: rewrite price_with_tax to take tax_rate as a parameter
tax_rate = 0.08

def price_with_tax(price, tax_rate):
    x = price + (price * tax_rate)
    return x

print(price_with_tax(20, tax_rate))

def add():
    count = count+ 1
    return count
print(add())
