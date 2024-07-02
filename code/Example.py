def is_queen_safe(board,x,y):
  for i,j in zip(range(x-1,-1,-1),range(y-1,-1,-1)):
    if board[i][j]==True:
      print("LUP")
      return False
  for i,j in zip(range(x-1,-1,-1),range(y+1,len(board))):
    if board[i][j]==True:
      print("RUP")
      return False
  for i in range(0,x):
    print(x,i)
    if board[i][y]==True:
      print("UP")
      return False
    
  return True


board=[
  [True, False, False, False],
[False, False, False, False],
[False, False, False, False],
[False, False, False, False]
]

print(is_queen_safe(board,0,1))