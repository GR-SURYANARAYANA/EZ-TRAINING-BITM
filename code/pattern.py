# * * * * *
# * *     *
# * *     *
# * * * * *
def pattern_one(n):
  for i in range(1,n+1):
    for j in range(1,n+1):
      if i == 1 or j == 1 or j == n or i == n or j == 2:  
        print("*" ,end=" ")
      else:
        print(" ",end=" ")
    print()
pattern_one(5)