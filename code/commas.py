import math
commas_count = 0
n = int(input())
i = 0
while n != 0:
  count = n % 1000
  commas_count = count * (1000 ** i) + commas_count
  i += 1
  n//=1000
print(commas_count + 1-1000)