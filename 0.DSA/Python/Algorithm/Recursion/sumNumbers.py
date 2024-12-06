def sumNumbers(n):
    if n==0:
        return n
    else:
        return n + sumNumbers(n-1)

print("Sum",sumNumbers(10))