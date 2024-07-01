ls = [
  [1,2,2,3],
  [3,1,4,2],
  [1,5,3,3],
  [1,2,1,1],
  [1,2,1,1],
  [1,2,1,1],
  [1,2,1,1],
  [1,2,1,1],
  [1,2,1,1]
]

dp = [[0]*len(ls[0]) for i in range(len(ls))]

cost = 0



for i in range(len(ls)):
  for j in range(len(ls[i])):
    if i == 0 and j ==0:
      dp[i][j] = ls[i][j]
    elif i == 0:
      dp[i][j] = dp[i][j-1] + ls[i][j]
    elif j == 0:
      dp[i][j] = dp[i-1][j] + ls[i-1][j]
    else:
      min_cost = min(dp[i][j-1],dp[i-1][j],dp[i-1][j-1])
      dp[i][j]=min_cost + ls[i][j]
print(dp[len(ls)-1][len(ls[0])-1])

for i in range(len(dp)):
  print(i,':',dp[i])

# def min_cost(dp,ls,i,j):
#   if i == len(ls):
#     return
#   for j in range(len(ls[i])):
#     if i == 0 and j ==0:
#       dp[i][j] = ls[i][j]
#     elif i == 0:
#       dp[i][j] = dp[i][j-1] + ls[i][j]
#     elif j == 0:
#       dp[i][j] = dp[i-1][j] + ls[i-1][j]
#     else:
#       min_cst = min(dp[i][j-1],dp[i-1][j])
#       dp[i][j]=min_cst + ls[i][j]
#   min_cost(dp,ls,i+1,0)

# min_cost(dp,ls,0,0)
# print(dp[len(ls)-1][len(ls[0])-1])
