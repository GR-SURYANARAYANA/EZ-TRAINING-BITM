"""
Single source all shortest path
"""
# d={
#     0:[(0,1,4),(0,7,8)],
#     1:[(1,0,4),(1,2,8),(1,7,11)],
#     2:[(2,1,8),(2,3,7),(2,5,4),(2,8,2)],
#     3:[(3,2,7),(3,4,9),(3,5,14)],
#     4:[(4,3,9),(4,5,10)],
#     5:[(5,2,4),(5,3,14),(5,4,10)],
#     6:[(6,5,2),(6,7,1),(6,8,6)],
#     7:[(7,0,8),(7,1,11),(7,6,1),(7,8,7)],
#     8:[(8,2,2),(8,6,6),(8,7,7)]
# }

# A-0 B -1 C -2  D -3  E-4  F - 5

d = {
  0:[(0,1,6),(0,2,4),(0,3,5)],
  1:[(1,4,-1)],
  2:[(2,1,-2),(2,4,3)],
  3:[(3,2,-2),(3,5,-1)],
  4:[(4,5,3)],
  5:[]
}
def min_source(cost,d):
  min =  float('inf')
  source = 0
  for i in d:
    if min >= cost[i]:
      source = i
      min = cost[i]
  return source
       
length = len(d)
cost = [float('inf')]*len(d)
print(cost)
source = int(input("Enter the source : "))
cost[source] = 0
while d:
  for i in d[source]:
    if i[1] in d:
      cost[i[1]] = min(cost[i[1]],cost[source]+i[2])
  d.pop(source)
  source = min_source(cost,d)
print(cost)

    
