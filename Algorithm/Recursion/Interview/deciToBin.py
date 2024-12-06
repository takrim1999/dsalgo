def dec2bin(n):
    if n==0:
        return ""
    else:
        return str(dec2bin(n//2)) + str(n%2)

print(dec2bin(8))