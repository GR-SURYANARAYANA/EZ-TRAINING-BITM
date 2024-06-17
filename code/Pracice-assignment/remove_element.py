nums = [3,2,2,3]
val = 3
d = {}
count = 0
for i in nums:
  if i == val:
    count += 1
  if i in d:
    d[i] += 1
  else:
    d[i] = 1
  
value = 0
for i in list(d.keys()):
  if i!= value:
    temp = (value + d[i])
    nums[value:temp] = [i]*temp
    value = temp
print(nums,count)


  

