import sys

n = int(input().strip())

#Loops 10 times and prints the product of x and n on seperate lines, to show multipliers
for x in range(1, 11):
    prod = n * x
    print(str(n) + " x " + str(x) + " = " + str(prod))
