result = []
def subset(given,answer):
  if not  given:
    return result.append(answer)
  ch = given[0]
  subset(given[1:],answer + ch)
  subset(given[1:],answer)

def subset_sum(given,answer,sum,target,index):
  if sum > target or index == len(given):
    return 
  if  sum == target :
    result.append(answer)
    return
  ch = given[index]
  subset_sum(given,answer + f'{ch}',sum+given[index],target,index+1)
  subset_sum(given,answer,sum,target,index+1)
  




# s ="abc"
subset_sum([4,5,6,7,8,9,10],"",0,15,0)
print(result)

