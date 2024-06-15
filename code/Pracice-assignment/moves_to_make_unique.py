"""
You are given an integer array nums. In one move, you can pick an index i where 0 <= i < nums.length and increment nums[i] by 1.

Return the minimum number of moves to make every value in nums unique.

The test cases are generated so that the answer fits in a 32-bit integer.

 

Example 1:

Input: nums = [1,2,2]
Output: 1
Explanation: After 1 move, the array could be [1, 2, 3].
Example 2:

Input: nums = [3,2,1,2,1,7]
Output: 6
Explanation: After 6 moves, the array could be [3, 4, 1, 2, 5, 7].
It can be shown with 5 or less moves that it is impossible for the array to have all unique values.
 

Constraints:

1 <= nums.length <= 105
0 <= nums[i] <= 105
Accepted
95,882
Submissions
179,619
"""
nums = [3,2,1,2,1,7]
nums = [1,1,2,2,3,7]
d = {}
for i in nums:
  if i not in d:
    d[i]  = 1
  else:
    d[i] = d[i] + 1
print(d)
moves = 0
for i in range(len(nums)):
  # print(nums[i],moves,d,nums)
  if d[nums[i]] >= 2:
    d[nums[i]] = d[nums[i]] - 1
    while nums[i] in d:
       moves += 1
       nums[i] += 1
    d[nums[i]] = 1
print(moves)

# nums.sort()
# print(nums)
# moves = 0
# for i in range(len(nums)-1):
# print(moves)