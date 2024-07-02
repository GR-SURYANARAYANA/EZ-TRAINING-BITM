

# def min_coin_required(amount,d,coins):
#   if not d:
#     print(coins)
#     return 
#   for i in d:
#     temp = dict(d)
#     temp.pop(i) 
#     min_coin_required(amount % i ,temp,coins + amount//i)

min = float('inf')
def min_coin_required(amount,d,coins,path):
  global min,min_path
  if amount < 0:
    return
  if amount == 0:
    if min >= coins:
      min = coins
      min_path = path
    return 
  for i in d: 
    min_coin_required(amount - i ,d,coins+1,path + f'+{i}')


d = {5:0,7:0,1:0}
min_coin_required(18,d,0,"")
print(min,min_path)