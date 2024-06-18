
d ={0:1,1:0,2:1}
t = 0
def fibo(n):
  global t
  t+=1
  if n in d:
    return d[n]
  else:
    d[n-1] = fibo(n-1)
    d[n-2] = fibo(n-2)
    return d[n-1] + d[n-2]

if __name__ == '__main__':
  print(fibo(int(input())),t)
