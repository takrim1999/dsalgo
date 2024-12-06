def factorial(n):
    assert n>=0 and int(n)==n, "Factorial cannot be negative" 
    if n==0:
        return 1
    else:
        return n*factorial(n-1)

print("Factorial",factorial(10))