import math
def is_prime_fast(number):
  if number <= 1 or (number > 2 and number % 2 == 0):
    return False
  else:
    for factor in range(2,int(math.sqrt(number))+1):
      if number % factor == 0:
        return False
    
  return True

def is_prime(n):
    max = int(math.sqrt(n))
    if  n == 2:
        return True
    elif n % 2 == 0 and n >= 2:
        return False
    elif n == 1:
        return False
    for x in range(3, max+1, 2):
        if n % x == 0:
            return False
    return True

for n in range(2,100):
  assert is_prime(n) == is_prime_fast(n)
  
