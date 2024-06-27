"""
Minimum spanning tree and minimum cost gives this algorithm 
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

min = float('inf')
source=destination = None
for i in range(len(Graph)):
  for j in range(len(Graph[i])):
    if Graph[i][j] >= 1 and min > Graph[i][j]:
      min = Graph[i][j]
      source = i
      destination = j

ls = []

visited = [False]*len(Graph)
visited[source] = True
visited[destination] =True
ls.append([source+1,destination+1,min])
cost = min
while False in visited:
  min = float('inf')
  for i in range(len(Graph)):
    if visited[i]:
      for j in range(len(Graph[i])):
        if Graph[i][j] >= 1 and min > Graph[i][j]  and not visited[j] :
          min = Graph[i][j]
          source = i
          destination = j
  visited[destination] = True
  ls.append([source+1,destination+1,Graph[source][destination]])
  cost+=Graph[source][destination]
print(ls,cost)

  
