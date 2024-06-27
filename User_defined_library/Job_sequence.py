profit = list(map(int,input("Enter the Profits : ").split(" ")))
deadline = list(map(int,input("Enter the Deadlines: ").split(" ")))
get_max = lambda x: max(x)
get_sorted = lambda x:x.sort()
d ={}

for  i in range(len(profit)):
  if profit[i] not in d:
    d[profit[i]] = [deadline[i]]
  else:
    d[i] = get_sorted(d[i] + [profit[i]])

selected = []
profit_made = 0
for i in d:
  if len(d[i]) > 1:
    count = 0
    while count!=len(d[i]):
      if len(selected) < d[i][count]:
        selected.append(f"{d[i]},{d[i][count]}")
        profit_made += i
  else:
    if len(selected) < d[i][count]:
        selected.append(f"{d[i]},{d[i][count]}")
        profit_made += i
  if len(d[i]) == get_max:
      break
    
print(selected,profit_made)
    





