num = [2,1,5]
carry = 806
i = len(num) - 1
while i >= 0 :
  sum = num[i] + carry
  num[i],carry = sum % 10,sum//10
  i -= 1
while carry>0:
  num.insert(0,carry%10)
  carry //= 10
print(num)