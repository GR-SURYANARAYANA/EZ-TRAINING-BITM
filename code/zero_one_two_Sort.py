ls = [2,1,0,1,1,2,0,0]
count_zero = 0
count_one = 0
count_two = 0
for i in ls:
  if i == 0:
    count_zero += 1
  elif i == 1:
    count_one += 1
  else:
     count_two += 1
i = 0
while i <count_zero:
  ls[i] = 0
  i+=1
temp = i
while i <temp + count_one:
  ls[i] = 1
  i+=1
temp = i
while i <temp + count_two:
  ls[i] = 2
  i+=1
print(ls)


"""
Functional Overloading

"""