a =[12,14,19,19,12]
a.sort()
print(a)
b = sorted([19,2,17,20,7])

# sum = 0
# for i in range(len(a)):
#   sum += abs(a[i]-b[i])
# print(sum)

import math


values = [4,3,100,5,13,25,17,15,61,37,85,25,65,29,53,65,85,41]
for c in values: 
  for i in range(1,(c//2 +1)):
    resutl = math.sqrt(c*c - i*i )
    if float(int(resutl)) == resutl:
      print(f"{c} {i}",True)
      break
  # print(False)
