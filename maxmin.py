numbers = [100, -100]

lowest = numbers[0]
highest = numbers[0]

for number in numbers:
    if number < lowest:
        lowest = number


for number in numbers:
    if number > highest:
        highest = number

print([lowest, highest])
