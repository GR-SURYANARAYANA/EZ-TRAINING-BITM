#Power to nth
def pow(n,m):
  if m == 0:
    return 1
  return n * pow(n,m-1)
  
n = 2
m = 3
print(pow(n,m))