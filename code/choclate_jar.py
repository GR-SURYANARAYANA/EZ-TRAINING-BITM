ls = map(int,input().split(" "))
sum = 0
for i in ls:
  result = i // 3 + 0 if i%3==0 else 1
  sum += result
print(sum) 