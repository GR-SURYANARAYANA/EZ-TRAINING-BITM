list = map(int,input().split(" "))
profit = 0
max = 0
for i in list:
  profit += i
  if max < profit:
    max = profit
  if profit < 0 :
    profit = 0
  
print(max)
