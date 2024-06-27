# # profits = list(map(int,input("Enter the profits : ").split(" ")))
# profits = [5,10,15,7,8,9,4]
# # weights = list(map(int,input("Enter the weights : ").split(" ")))
# weights = [1,3,5,4,1,3,2]
# # capacity = int(input("Enter the capacity : "))
# capacity = 15
# result = [[0 for i in range(capacity+1)]for j in range(len(profits)+1)]
#
# # print(profits,weights,result)
# n=len(profits)
# for i in range(1,n+1):
#   for c in range(1,capacity+1):
#     if c-weights[i-1] < 0:
#       result[i][c] = result[i - 1][c]
#     else:
#       result[i][c] = max(result[i-1][c],profits[i-1] + result[i-1][c-weights[i-1]])
#
#
# for i in result:
#   print(i)



"""
P: 5 10 15 7 8 9 4
W: 1 3 5 4 1 3 2
C=15
"""

a = [[[0]*2]*2]*2
# a= [[33,33],[33,33]]
print(a)
a[0][1][0] = 10
a[0][1][1] = 15

print(a)
