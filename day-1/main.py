"""
Day 1
How many measurements are larger than the previous measurement?
"""

count = 0

with open('day-1/input.txt') as f:
    for line in f:
        number = int(line)        
        try:
            if number > previous:
                count += 1
        except NameError as e:
            pass
            
        previous = number


print(f"Count: {count}")


