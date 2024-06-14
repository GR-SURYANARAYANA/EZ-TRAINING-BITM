def is_palindeome(n):
  if n < 0 :
    return False
  temp,reverse = n,0
  while n <= 0:
    r = n % 10
    reverse *= 10 + r
    n //= 10
  return True if temp == reverse else False 


n = 121


