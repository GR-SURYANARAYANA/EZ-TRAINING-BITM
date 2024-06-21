import math

ls = list(map(int,input().split(" ")))
sub_sum = -1 * math.inf
# for i in range(len(ls)):
#   for j in range(i+1,len(ls)):
#     a = ls[i:j+1]
#     result = sum(a)
#     if result > sub_sum:
#       sub_sum = result
# print(sub_sum)

# total_sum = sum(ls)
# max_sum = total_sum
# for i in range(len(ls)):
#   total_sum += ls[i]
#    for j in range(i+1,len(ls)):
#     temp_sum = total_sum + ls[i] 

# Kaden's Algorithms
curr_sum = 0
max_sum = 0
for i in ls:
  curr_sum += i
  if max_sum < curr_sum:
    max_sum = curr_sum
  if curr_sum < 0:
    curr_sum = 0
print(curr_sum)
