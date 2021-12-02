"""
Day 2 
Calculate the horizontal position and depth you would have after following the planned course.
"""

with open("day-2/input.txt") as f:
    commands = [line for line in f]

# Part 1
x = 0
y = 0

for c in commands:
    dir, n = c.split(" ")
    n = int(n)

    if dir == "down":
        y += n
    elif dir == "up":
        y -= n
    else:
        x += n

print(f"Part 1 - Multiplication: {x*y}")


# Part 2
x = 0
y = 0
aim = 0

for c in commands:
    dir, n = c.split(" ")
    n = int(n)

    if dir == "down":
        aim += n
    elif dir == "up":
        aim -= n
    else:
        x += n
        y += aim * n

print(f"Part 2 - Multiplication: {x*y}")
