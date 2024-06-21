from library import Queue


def dfs(d,visited,index = 1):
  if not visited[index]:
      visited[index] = True
      for i in d[index]:
         if not visited[i[1]]:
            dfs(d,visited,i[1])
      print(index,end = " ")
    
  
         

def bfs(d,visited,index = 1):
  for i in d:
      print(i,end =" ")
      visited[i] = True
      for k in d[i]:
          if not visited[k[1]]:
            print(k[1],end = " ")
            visited[k[1]] = True
          




d = {1:[(1,2,0),(1,3,0)],
     2:[(2,1,0),(2,7,0)],
     3:[(3,1,0),(3,6,0),(3,5,0)],
     4:[(4,7,0),(4,8,0)],
     5:[(5,3,0),(5,7,0)],
     6:[(6,3,0),(6,8,0)],
     7:[(7,2,0),(7,5,0),(7,4,0)],
     8:[(8,4,0),(8,6,0),(8,8,0)]
    }

d = {
  1:[(1,2,0),(1,3,0)],
  2:[(2,1,0),(2,5,0)],
  3:[(3,1,0),(3,4,0),(3,6,0)],
  4:[(4,3,0)],
  5:[(5,2,0),(5,7,0),(5,10,0),(5,13,0)],
  6:[(6,3,0),(6,7,0)],
  7:[(7,5,0),(7,6,0),(7,8,0),(7,9,0)],
  8:[(8,7,0)],
  9:[(9,7,0),(9,12,0)],
  10:[(10,5,0),(10,11,0)],
  11:[(11,10,0)],
  12:[(12,9,0),(12,13,0)],
  13:[(13,5,0),(13,12,0)]
    }

visited = [False] * (len(d) + 1)
ls = []
# print(d[1])

bfs(d,visited,1)