# def is_list_sorted(ls,i,j):
#   if i >= j:
#     return True
#   if ls[i] > ls[j]:
#     return False
#   return is_list_sorted(ls,i+1,j-1)

def is_list_sorted(ls,i,j):
  if i>=len(ls)-1:
    return True
  if ls[i] > ls[i+1]:
    return False
  return is_list_sorted(ls,i+1)



ls = [1,2,5,4,5,6,7,8,9,10]
ls = [1]
print(is_list_sorted(ls,0))
