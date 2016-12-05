# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13,
# we can see that the 6th prime is 13.
# What is the 10 001st prime number?
def isprime(number):
  result = True
  for i in range(2, number // 2):
    if number % i == 0:
      result = False
  return result

count = 0
for i in range(9883, 10003):
  if isprime(i):
    count += 1
    print(i)
print(count)
