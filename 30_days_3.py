import sys

N = int(input().strip())

if N % 2 == 0 and (N < 6 or N > 20):
    print("Not Weird")
else:
    print("Weird")
