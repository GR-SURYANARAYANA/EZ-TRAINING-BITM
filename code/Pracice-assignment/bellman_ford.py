"""
To overcome the dijikstras drawback of negative values we use bellmanford 
"""

d = {
  0:[(0,1,6),(0,2,4),(0,3,5)],
  1:[(1,4,-1)],
  2:[(2,1,-2),(2,4,3)],
  3:[(3,2,-2),(3,5,-1)],
  4:[(4,5,3)],
  5:[]
}

# pair_list = [j[0],j[1] for j in d[a] for a in d]
pair_list = []
for i in d:
  for j in d[i]:
    a = j[0],j[1],j[2]
    pair_list.append(a)

cost = [float('inf')]*len(d)
source = int(input(""))
cost[source] = 0
for i in range(len(d)):
  for i in pair_list:
    source = i[0]
    destination = i[1]
    weight = i[2]
    cost[destination] = min(cost[source] + weight,cost[destination])
print(cost)
