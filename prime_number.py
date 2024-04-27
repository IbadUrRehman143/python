

"""
5 --> 1, 5
   2
  ____
5/ 10
   10
 -----
   0

10
2, 3, 4, 5, 6, 7, 8, 9   
"""

def is_prime(num):
    for i in range(2, num):
        if (num % i == 0): 
            return False
    
    return True

print(is_prime(21))
        