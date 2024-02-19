#Factorial Finder
#The Factorial of a positive integer, n, is defined as the product of the sequence n, n-1, n-2, ...1 and the factorial of zero, 0, is defined as being 1.
#Solve this using both loops and recursion.

#using loops:
def factorialloop(n):
    total = 1
    for i in range(1,n+1):
        total *= i
    print(f'{n} factorial is {total} (calculated with loop)')

#using recursion:
def factorialrecursion(n):
    if n-1 > 0:
        total = n * factorialrecursion(n-1)
    else:
        total = 1
    return total

num = int(input("Please enter the number you'd like to know the factorial of: "))
factorialloop(num)
print(f'{num} factorial is {factorialrecursion(num)} (calculated with recursion)')
