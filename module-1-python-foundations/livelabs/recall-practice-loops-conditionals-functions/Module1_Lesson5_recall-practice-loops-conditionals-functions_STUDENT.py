#!/usr/bin/env python3
"""Day 5 code-along: Recall & Practice. Run: python3 <file> or ./<file>"""

# Example

grid = [[1,2],[3,4],[5,6]]
total = 0
#print(grid)
for row in grid:
    for value in row:
        if value % 2 == 0:
            total += value
print(total)

#create a function that calculates the area using the follow: area(3,4)
def area(l,w):
    return l * w 

print(area(3,4))
print(area(9,6))

# ===== 1. Loop + Conditional + Function, Together =====
# Count how many scores pass a threshold of 70. Here the answer is 3.
print('----- 1. Loop + Conditional + Function, Together -----')
# TODO: define count_passing(scores, threshold)
# TODO: return how many scores are >= threshold
def count_passing(scores, threshold):
    count = 0
    for score in scores:
        if score >= threshold:
            count += 1
    return count        

print(count_passing([55, 82, 91, 40, 76], 70))

# TODO: call it with [55, 82, 91, 40, 76] and 70; print the result

def count_long_shifts(hours):
    count = 0
    for h in hours:
        if h >= 4:
            count += 1
        return count

print(count_long_shifts([3,4,6,2,5]))