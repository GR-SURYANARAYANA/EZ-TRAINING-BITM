import math
def check_prime(n):
  limit = int(math.sqrt(n))+1
  for i in range(2,limit):
    if n % i == 0:
      return False
  return True  

n = int(input())
if check_prime(n) :
  print("valid message")
else:
  print("invalid message")