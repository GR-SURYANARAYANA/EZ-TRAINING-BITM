ctr=[0]

def is_queen_safe(board,x,y):
  for i,j in zip(range(x-1,-1,-1),range(y-1,-1,-1)):
    if board[i][j]==True:
      return False
  for i,j in zip(range(x-1,-1,-1),range(y+1,len(board))):
    if board[i][j]==True:
      return False
  for i in range(0,x):
    if board[i][y]==True:
      return False
    
  return True




# def is_queen_safe(board,x,y):
#   return check_diagonal(board,x,y) and check_verticle(board,x,y)
  
  
def N_Queen(board,i):
  if i == len(board):
    ctr[0]+=1
    for x in board:
      print(x)
    print()
    return True
  
  for j in range(len(board)):
    board[i][j] = True
    if is_queen_safe(board,i,j)==True:
      N_Queen(board,i+1)
    board[i][j] = False
 

  
n = 4#int(input("Enter the number of queens : "))
board = [[False]*n for i in range(n)]
N_Queen(board,0)
print(ctr)
