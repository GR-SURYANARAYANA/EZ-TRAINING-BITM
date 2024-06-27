"""

Minimum cost to visit all edges
"""


Graph = [
    [0, 7, -1, -1, -1, -1, -1, 2, -1, -1],
    [7, 0, 4, 1, -1, 5, -1, -1, -1, -1],
    [-1, 4, 0, -1, -1, -1, -1, 8, -1, -1],
    [-1, 1, -1, 0, 6, 8, 3, 3, -1, -1],
    [-1, -1, -1, 6, 0, -1, -1, 6, 8, -1],
    [-1, 5, -1, 8, -1, 0, -1, -1, -1, -1],
    [-1, -1, -1, 3, -1, -1, 0, -1, 9, 2],
    [2,-1,8,3,6, 1, -1, 0, -1, -1],
    [-1,-1,-1,-1,8,-1,9,-1,0,-1],
    [-1,-1,-1,-1,-1,-1,2,-1,-1,0]
  ]

unsorted = []

for i in range(len(Graph)):
  for j in range(len(Graph[i])):
    if Graph[i][j] > 0:
      unsorted.append([i,j,Graph[i][j]])

for i in range(len(unsorted)):
  for j in range(len(unsorted)):
    if unsorted[i][2] < unsorted[j][2]:
      unsorted[i],unsorted[j] = unsorted[j],unsorted[i]
# print(unsorted)  

visited = [False]*len(Graph)
list = []
i = 0
cost = 0
while i!=len(unsorted) and not all(visited):
  source = unsorted[i][0]
  dest = unsorted[i][1]
  path_cost = unsorted[i][2]
  if not visited[source] or not visited[dest]:
    if not visited[source]:
      visited[source] =True
    if not visited[dest]:
      visited[dest] = True
    list.append(unsorted[i])
    cost += path_cost
  i+=1
  
print(list,cost)  

