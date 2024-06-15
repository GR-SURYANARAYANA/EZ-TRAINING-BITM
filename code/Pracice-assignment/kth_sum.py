def sum(ls,start,end):
  sum = 0
  for i in range(start,end):
    sum += ls[i]
  return sum


k =int(input())
ls = list(map(int,input().split(" ")))

max = 0
for i in range(len(ls) - k):
  temp = sum(ls,i,i+3)
  if max < temp:
    result = ls[i:i+k]
    max = temp
print(result,max)

"""
3
2 4 3 5 6 3 4 6 7 1 2 5
"""
