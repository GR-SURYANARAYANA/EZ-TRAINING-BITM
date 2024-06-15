def sum(ls,start,end):
  sum = 0
  for i in range(start,end):
    sum += ls[i]
  return sum

k = int(input())
ls = list(map(int,input("").split(" ")))
if len(ls) <= k:
  max = sum(ls,0,len(ls))
  print(ls,max)
else:
  max = sum(ls,0,k)
  temp = max
  index = 0
  count = 0
  for i in range(k,len(ls)):
    temp = temp + ls[i] - ls[count]
    if  max < temp:
      index = i
      max = temp
    count += 1
  print(ls[index - k + 1:index +1],max)

