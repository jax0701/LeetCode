"""Given a non-negative integer num, repeatedly add all its digits until the result has only one digit.
For example:
Given num = 38, the process is like: 3 + 8 = 11, 1 + 1 = 2. Since 2 has only one digit, return it.a"""

def add_digits(num):
    sum = 0
    while (num//10) > 0:
        while (num//10)>0:
            sum = sum + (num//10)
            num = num%10
            if num < 10:
                sum = sum + num
        num = sum
        sum = 0
    return num

print add_digits(9)
      


