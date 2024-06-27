import math


def find_max(d):
  max = -1* math.inf
  item = 0
  for i in d:
    if d[i] > max:
      max = d[i]
      item = i
  return item

p  = list(map(int,input("Enter the prices : ").split(" ")))
w  = list(map(int,input("Enter the Weights : ").split(" ")))
pw = {(i+1):p[i]/w[i] for i in range(len(p))}
capacity = int(input("Enter the capacity : "))
selected = []
filled = 0
profit = 0
for i in range(len(p)):
  max_item = find_max(pw)
  if (capacity-filled) > 0:
    if filled <= capacity and w[max_item - 1 ] <= (capacity-filled):
      filled += w[max_item-1]
      profit += p[max_item-1]
      selected.append(max_item)
  else:
    break
  pw.pop(max_item) 

print(selected,profit)

"""
5 10 15 7 8 9 4
1 3 5 4 1 3 2
"""