# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
stop = False
number = 2520
while not stop:
    result = []
    for i in range(1, 21):
        if number % i == 0:
            result.append(True)
        else:
            result.append(False)
    if False not in result:
        stop = True
        print(number)
    number += 20
