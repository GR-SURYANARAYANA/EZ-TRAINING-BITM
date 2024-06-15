
"""
In a dice game 2 players are playing P1 and P2. both player is rolling the dice one by one and getting score 
and that score is getting added to the total score of the player.

A player can get a chace of rolling the dice again if his total Score is Disivible by 2 and dice face is not divisible by 2.

If the player having the dice face and total Score both are even then the player will not get the chace of rolling the dice again.

If the player Score is odd and the dice face is also odd then the dice face value will be decreased from the total socre of the player

You will be given a list of 10 dice face number as input find the will and also print the total score of each player.
"""
def iseven(n):
  return n%2 == 0

n = 10
dice_played = [int(input()) for i in range(n)]
score = [0,0]
play = 1
for i in range(0,n,2):
    score_check = iseven(score[play-1])
    dice_check = iseven(dice_played[i])
    if not(score_check) and not(dice_check):
      score[play-1] -= dice_played[i]
    else:
      score[play-1] += dice_played[i]

    if  score_check and not(dice_check):
       continue
    
    play = (2 if play == 1 else 1)
print("scores of players are as follows : ",score)
       
      