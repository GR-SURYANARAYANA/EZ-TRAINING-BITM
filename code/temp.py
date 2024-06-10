import math
ls = list(map(int,input("Armstrong list ").split(" ")))
print(ls)
for i in range(len(ls)):
  ls[i] = sum([int(j) ** int(math.log10(ls[i]) + 1) for j in str(ls[i])])
print(ls)