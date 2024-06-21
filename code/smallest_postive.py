import math


ls = map(int,input().split(" "))
smallest = math.inf

for i in ls:
  if i>0 and smallest > i:
    smallest = i

print((0 if smallest == math.inf else smallest))