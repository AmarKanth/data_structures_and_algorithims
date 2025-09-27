"""
Write a program to print prime numbers
"""
for num in range(2, 10):
    for i in range(2, num):
        if num%i == 0:
            break
    else:
        print(num)


"""
Write a program for n factorial
"""
def factorial(n):
    if n == 0:
        return 1
    return factorial(n-1)*n

res = factorial(4)
print(res)


"""
Write a program for Fibonacci series
"""
def fibonacci(n):
    if n in [0,1]:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

res = fibonacci(10)
print(res)

n = 9
num1 = 0
num2 = 1
next_number = num1 + num2
counter = 1
while counter <= n:
    print(num2)
    num1, num2 = num2, next_number
    next_number = num1 + num2
    counter += 1


"""
Write a program to sum of digits in the number
"""
def sum(num):
    if num == 0:
        return 0
    return sum(num//10) + num%10

res = sum(11)
print(res)


"""
Write a program to reverse the digits in the number
"""
def reverse(num, reversed_num):
    if num == 0:
        return reversed_num
    quotient, reminder = num//10, num%10
    rn = reversed_num*10 + reminder
    return reverse(quotient, rn)

res = reverse(123, 0)
print(res)


"""
Write a program to power of number in recursive method
"""
def power(base, exp):
    if exp == 0:
        return 1
    if exp == 1:
        return base
    return base*power(base, exp-1)

res = power(3, 3)
print(res)


"""
How to find GCD (Greatest common divisor) of two numbers using recursion
"""
def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a%b)

res = gcd(48, 18)
print(res)


"""
How to convert decimal to binary number using recursion
"""
def decimalToBinary(n):
    if n == 0:
        return 0
    return n%2 + 10 * decimalToBinary(n//2)

res = decimalToBinary(13)
print(res)
