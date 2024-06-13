voters = map(int,input("Enter the Voters list : ").split(" "))
contestent = [0] * 7
for i in voters:
  contestent[i-1] += 1

#finding the max values
max = 0
for i in range(len(contestent)):
   if max < contestent[i] :
      max = contestent[i]



# findind people with max indexes
collide  = []
for i in range(len(contestent)):
   if contestent[i] == max:
      collide.append(i+1)
      
print(f"No collide {collide[0]} is the winner " if len(collide) == 1 else f"candidates who collided are {collide}")