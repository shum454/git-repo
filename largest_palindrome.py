# A palindromic number reads the same both ways.
# The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
# Find the largest palindrome made from the product of two 3-digit numbers.
def is_palindrome(number):
    string = str(number)
    result = ""
    i = 0
    k = len(string) - 1
    while i != len(string):
        result += string[k]
        k -= 1
        i += 1
    if result == string:
        return True
    else:
        return False
result = 0
for i in range(1000):
    if i == 0:
        continue
    for j in range(1000):
        if j == 0:
            continue
        number = i * j
        if is_palindrome(number):
            if result < number:
                result = number
print(result)
