m = int(input("Introduceti m: "))
n = int(input("Introduceti n: "))

def factorial(x):
    factor = 1
    for i in range(1,x-1):
        factor = factor * 1
    return factor
print(factorial(n) / factorial(m) * factorial(n - m) )