def binary_search(ls,target,start,end):
  if start > end or end > len(ls):
    return -1
  mid = (start+end)//2
  if ls[mid] == target:
    return mid
  elif target > ls[mid]:
    return binary_search(ls,target,mid+1,end)
  else:
    return binary_search(ls,target,start,mid-1)


ls = [1,2,3,4,5,6,7,8,9,10]
print(binary_search(ls,10,0,len(ls)-1))