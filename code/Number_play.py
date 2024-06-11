ls = [4,0,5,0,1,9,0,0]
i = 0
j = 0
while i!=len(ls) and j <len(ls):
  if ls[i]!=0:
    i += 1
    j = i 
  else:
     if ls[j] != 0:
       temp = ls[i]
       ls[i] = ls[j]
       ls[j] = temp
       i += 1
     j +=1 
print(ls) 




   