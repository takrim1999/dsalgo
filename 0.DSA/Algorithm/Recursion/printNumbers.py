def printNumbers(n):
    if n==0:
        print(0)
    else:
        printNumbers(n-1)
        print(n)
        
printNumbers(10)