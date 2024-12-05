import sys

inp = "".join(sys.stdin.readlines()).strip().split("\n")[2::2]

for array in inp:
    print([int(i) for i in array.split()])