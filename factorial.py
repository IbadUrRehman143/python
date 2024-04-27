"""
Factorial
forward
5! --> 5 * 4 * 3 * 2 * 1 = 120
7! --> 7 * 6 * 5 * 4 * 3 * 2 * 1

reversed
5! --> 1 * 2 * 3 * 4 * 5
"""

n = 7
factorial = 1
for i in range(1, n+1):
    factorial = factorial * i

print(factorial)