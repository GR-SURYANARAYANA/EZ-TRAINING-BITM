def getAmstrong(n,digit):
  sum = 0
  while n > 0:
    sum += ((n%10) ** digit)
    n//=10
  return sum

def getDigit(num):
  count = 0
  while  num > 0:
    count+=1
    num = num//10
  return int(count)

ls = list(map(int,input("Armstrong list ").split(" ")))
result = [getAmstrong(n,getDigit(n)) for n in ls ]
print(result)  
#Note: Beaware of the datatypes