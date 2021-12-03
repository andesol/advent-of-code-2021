"""
Day 2
Use the binary numbers in your diagnostic report to calculate 
the gamma rate and epsilon rate, then multiply them together. 
What is the power consumption of the submarine?
"""

with open("day-3/input.txt") as f:
    ls = f.readlines()
    numbers = [l.rstrip() for l in ls]
    numbers = [[int(d) for d in n] for n in numbers]

# Part 1
counter = [0] * len(numbers[0])
for n in numbers:
    n1 = [-1 if d == 0 else 1 for d in n]

    counter = [x + y for x, y in zip(counter, n1)]

g = [1 if i > 0 else 0 for i in counter]
e = [0 if i > 0 else 1 for i in counter]


gamma = int("".join(map(str, g)), 2)
epsilon = int("".join(map(str, e)), 2)
print(f"Part 1: {gamma * epsilon}")

# Part 2
numbers1 = numbers
for i in range(0, len(numbers[0])):
    if len(numbers1) == 1:
        break

    counter = 0
    for n in numbers1:
        n1 = 1 if n[i] == 1 else -1
        counter += n1

    if counter < 0:
        numbers1 = [n for n in numbers1 if n[i] == 0]
    else:
        numbers1 = [n for n in numbers1 if n[i] == 1]


o2 = int("".join(map(str, numbers1[0])), 2)


numbers2 = numbers
for i in range(0, len(numbers[0])):
    if len(numbers2) == 1:
        break
    counter = 0
    for n in numbers2:
        n1 = 1 if n[i] == 1 else -1
        counter += n1

    if counter < 0:
        numbers2 = [n for n in numbers2 if n[i] == 1]
    else:
        numbers2 = [n for n in numbers2 if n[i] == 0]


co2 = int("".join(map(str, numbers2[0])), 2)
print(f"Part 2: {o2 * co2}")
