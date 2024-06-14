import math
def find_prime(n):
  for i in range(2,int(math.sqrt(n) + 1)):
    if n % i == 0:
      return False
  return True


def find_smallest_prime(n):
  while True:
    n = n + 1
    if find_prime(n):
      return n

def find_sum(n,flag = "sum"):
  a = [False] * (n+1)
  for i in range(2,n):
    mul = 2
    if a[i] == False:
      while i * mul <= n:
        a[i*mul] = True
        mul += 1
  if flag == "sum":
    sum = 0
  # print(a)
    for i in range(len(a)):
      if a[i] == False:
        sum += i
  return sum if flag=="sum" else a


n = int(input())
nex_prime = find_smallest_prime(n)
print("Next Prime is ",nex_prime)
print("find sum upto N and next smallest_number ",find_sum(nex_prime))
print("Sum in between number of two prime number is : ",sum(range(n + 1,nex_prime)))
nex_prime2 = find_smallest_prime(n)
product = nex_prime * nex_prime2
print(f"Find prime of next 2 smallest prime and check its product is prime.. then {product} is it prime ? : ",find_prime(product))

