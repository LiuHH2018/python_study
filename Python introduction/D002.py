# Q002
# Tag: recursion(input,factorial)
# Description: Write a program which can compute the factorial of a given numbers.
#              The results should be printed in a comma-separated sequence on a single line.
#              Suppose the following input is supplied to the program:
#
# Suppose the following input is supplied to the program:
# 8
# Then, the output should be:
# 40320


def fact(n):
    if n==1:
        return 1
    return n * fact(n - 1)

n = int(input("Pelase input a number:"))
print(fact(n))
  
