def linear_search(ls,target,index=0):
  if index == len(ls):
    return -1
  return (index if ls[index] == target else linear_search(ls,target,index+1))

def find_last(ls,target,index):
  if index == -1:
    return -1
  return (index - len(ls) if ls[index] == target else find_last(ls,target,index-1))

def find_ele_index(ls,target,index):
  if index == len(ls):
    return []
  return ([index] if target== ls[index] else [])+ find_ele_index(ls,target,index+1)
  

ls = [1,2,10,20,39,40,60,10,10,70,-2,20,10,-5,-7]
print(find_ele_index(ls,10,0))