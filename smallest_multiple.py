# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
stop = False
number = 10
while not stop:
    for i in range(1, 11):
        if number % i != 0:
            continue
        else:
            if i == 10:
                print(number)
                stop = True
            else:
                continue
    number += 1
print(number)
