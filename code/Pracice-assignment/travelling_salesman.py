G = [
  #1,2,3,4,5
  [0,4,7,5,5],#1
  [4,0,2,3,8],#2
  [7,2,0,3,4],#3
  [5,3,3,0,6],#4
  [5,8,4,6,0]#5
]


# def travel_salesman(source,dest,visited,G,count):
#   if count == len(G):
#     return G[dest][source]
  
#   visited[source] = True
#   for i in range(len(G)):
#     if not visited[i]:

visited = [False] * len(G)
source = 0
cost = 0
destination = None
while not all(visited):
  visited[source] = True
  min = float('inf')
  for i in range(len(G)):
    if not visited[i] and min > G[source][i]:
      min = G[source][i]
      destination = i
  cost += G[source][destination]
  source = destination

print("Minimum cost is ",cost+G[destination][0])
      

      




