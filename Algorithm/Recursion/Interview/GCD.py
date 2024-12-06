def gcd(a,b):
    if a<0:
        a = -1*a
    if b<0:
        b = -1*b
    if a % b == 0:
        return b
    else:
        return gcd(b,a%b)

print(gcd(18,-48))