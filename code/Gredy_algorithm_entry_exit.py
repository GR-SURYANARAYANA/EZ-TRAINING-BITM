# ls = [[1,2,2,3],[3,1,4,2],[1,5,3,3],[1,2,1,1]]
ls = [
  [1,2,5],
  [2,3,4],
  [5,6,7]
]

cost = 0
i = 0
j = 0
# while i<=len(ls)-1 and j<=len(ls[0])-1:
#   if i==len(ls)-1:
#     j+=1
#     while j!=len(ls[0]):
#       cost += ls[i][j]
#       j+=1
#   elif j==len(ls)-1:
#     i+=1
#     while i!=len(ls):
#       cost += ls[i][j]
#       i+=1
#   else:
#     i,j = ([i,j+1] if ls[i+1][j] > ls[i][j+1] else [i+1,j])
#     cost+=ls[i][j]

while i!=len(ls)-1 and j!=len(ls[0])-1:
  cost+=ls[i][j]
  i,j = ([i,j+1] if ls[i+1][j] > ls[i][j+1] else [i+1,j])
    
if i==len(ls)-1:
    while j!=len(ls[0]):
      cost += ls[i][j]
      j+=1
elif j==len(ls)-1:
    while i!=len(ls):
      cost += ls[i][j]
      i+=1


print(cost)