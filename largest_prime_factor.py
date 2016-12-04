# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?
#high = 13195
#for num in range(high):
#    num += 1
#    if high % num == 0:
#        for x in range(num):
#            y = x + 1
#            if num % y == 0:
#                continue
#            else:
#                print(num)
finish = 600851475143
for number in range(finish // 2):
    if number < 2:
        continue
    if finish % number == 0:
        i = 2
        is_prime = True
        while i != number:
            if number % i == 0:
                is_prime = False
            i += 1
        if is_prime:
            print(number, " is a prime!")
        else:
            continue
