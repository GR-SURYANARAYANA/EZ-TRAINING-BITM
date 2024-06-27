p  = list(map(int,input("Enter the prices : ").split(" ")))
w  = list(map(int,input("Enter the Weights : ").split(" ")))
pw = [p[i]/w[i] for i in range(len(p))]
capacity = int(input("Enter the capacity : "))

for i in range(len(pw)):
  for j in range(i+1,len(pw)):
    if pw[i] < pw[j]:
      pw[i],pw[j] = pw[j],pw[i]
      p[i],p[j] = p[j],p[i]
      w[i],w[j] = w[j],w[i]

bag_filled = 0
sum = 0
for i in range(len(w)):
  if bag_filled <= capacity:
    if w[i] <= (capacity - bag_filled):
      print(p[i],w[i])
      sum += p[i]
      bag_filled += w[i]
print("Maximized profit is : ",sum)

    

"""
5 10 15 7 8 9 4
1 3 5 4 1 3 2
"""