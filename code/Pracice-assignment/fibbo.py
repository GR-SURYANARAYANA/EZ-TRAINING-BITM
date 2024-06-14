n = int(input())
a,b = 0,1
if n >= 1:
    a = 0
    print(a,end=" ")
if n >= 2:
    b == 0
    print(b,end=" ")
if n > 2:     
  for i in range(n-2):
    a,b = b,a+b
    print(b,end = " ")
