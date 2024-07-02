d= {1:0,5:0,7:0}

amount = 18
for i in [7,5,1]:
  d[i] = amount // i
  amount =amount % i

print(d)