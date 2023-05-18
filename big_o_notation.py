"""
Big o is the language and metric we used to describe the efficiency of algorithms. 
1. Big O it is a complexity that is going to be less or equal to worst case.
2. Big Omega it is a complexity that is going to be at least more than the best case.
3. Big Theta it is a complexity that is within bounds of the worst and the best cases.
"""

"""
Complexity 	Name     		Sample
O(1)       	Constant 		Accessing a specific element in array and if statements
O(N) 		Linear			Loop through array elements (0...N)
O(LogN) 	Logarithmic 	Find an element in sorted array
O(N**2) 	Quadratic 		Looking for every index in the array twice
O(2**N) 	Exponential 	Double recursion in Fionacci
"""

"""
O(LogN) :-

log2(depth) = n ===> b**depth = n
Here depth is number of levels n is devided into.
Binary Logarithm default base number is 2.
"""

"""
Big O Complexity
1. O(Log N), O(1)
2. O(N)
3. O(N Log N)
4. O(N**2)
5. O(2**N)
6. O(N!)
"""

"""
O(1)+O(1)+O(n)+O(1)+O(n)+O(1)+O(1)
2O(n)+5O(1)
2O(n)
O(n)

time complexity is O(n)
"""
def foo(array):
    sum = 0                                     #-----O(1)
    product = 1                                 #-----O(1)

    for i in array:                             #-----O(n)
        sum += i                                #-----O(1)
    
    for i in array:                             #-----O(n)
        product *= i                            #-----O(1)
    
    print(f"Sum = {sum}, Product = {product}")  #-----O(1)


"""
outer loop n
inner loop n
n*n
n**2

time complexity is O(n**2)
"""
def printPairs(array):
    for i in array:
        for j in array:
            print(f"{str(i)} , {str(j)}")


"""
outer loop n-1
inner loop n-2

(n-1)(n-2)
n**2-2n-n+2 
n**2

time complexity is O(n**2)
"""
def printUnorderdPairs(array):
    n = len(array)
    for i in range(0, n):
        for j in range(i+1, n):
            print((array[i], array[j]))

"""
a = len(arrayA)
b = len(arrayB)

time complexity is O(ab)
"""
def printUnorderedPairs(arrayA, arrayB):
    for i in range(len(arrayA)):
        for j in range(len(arrayB)):
            if arrayA[i] < arrayB[j]:
                print(f"{arrayA[i]}-{arrayB[j]}")

"""
a = len(arrayA)
b = len(arrayB)
100000 = constant

time complexity is O(ab)
"""
def printUnorderedPairs(arrayA, arrayB):
    for i in range(len(arrayA)):
        for j in range(len(arrayB)):
            for k in range(0, 100000):
                if arrayA[i] < arrayB[j]:
                    print(f"{arrayA[i]}-{arrayB[j]}")

"""
n/2
n

time complexity is O(n)
"""
def reverse(array):
    for i in range(0, len(array)//2):
        other = len(array)-i-1
        temp = array[i]
        array[i] = array[other]
        array[other] = temp
    return array

"""
the following statements are equivalent of O(n)
1. O(N+P)
2. O(2N)
3. O(N+logN)

the following statements are not equivalent of O(n)
4. O(N+NlogN)
5. O(N+M)
"""

"""
n! = 1*2*3*...*n

M(n)    = O(1)+M(n-1)
M(0)    = O(1)
M(n-1)  = O(1)+M((n-1)-1)
M(n-2)  = O(1)+M((n-2)-1)

M(n)= 1 + M(n-1)
    = 1 + (1+M((n-1)-1))
    = 2 + M(n-2) 
    = 2 + 1 + M((n-2)-1)
    = 3 + M(n-3)

    =a+M(n-a)
    =n+M(n-n)
    =n+1
    =n

time complexity is O(n)
"""
def factorial(n):           #----> M(n)
    if n == 0:
        return 1            #----> O(1)
    return factorial(n-1)*n #----> M(n-1)

"""
fib(1) ---> 2**1
fib(2) ---> 2**2
fib(3) ---> 2**3
fib(4) ---> 2**4
fib(n) ---> 2**n

=(2**1)+(2**2)+(2**3)+...+(2**n)
=(2**n+1)-2
=2**n

time complexity is 2**n
"""
def allFib(n):
    for i in range(n):
        print(f"{i}-{fib(i)}")

def fib(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    return fib(n-1) + fib(n-2)