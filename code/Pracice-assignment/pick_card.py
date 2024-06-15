import math


n =  [1,2,3,4,5,6,7,8,9,10,2]
d = {}
min = math.inf 
value = -1
for i in range(len(n)):
  if  n[i] in d:
    temp = i - d[n[i]]
    d[i] = i
    if min >= temp:
      min = temp
      value = n[i]
  d[n[i]] = i
print(min + 1,value)
