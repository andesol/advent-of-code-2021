"""
Day 1
How many measurements are larger than the previous measurement?
"""

with open("day-1/input.txt") as f:
    numbers = [int(line) for line in f]


def count_increases(numbers):
    count = 0
    for n in numbers:
        try:
            if n > previous:
                count += 1
        except NameError:
            pass

        previous = n

    return count


# Part 1
count1 = count_increases(numbers)
print(f"Part 1: Count: {count1}")


# Part 2
measurements = []
for i, item in enumerate(numbers):
    try:
        m = item + numbers[i + 1] + numbers[i + 2]
    except:
        pass

    measurements.append(m)

count2 = count_increases(measurements)
print(f"Part 2: Count: {count2}")
