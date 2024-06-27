memory = [0,1]
def fibo(n):
  global memory
  if len(memory) <= n:
    memory.append(fibo(n-2) + fibo(n-1))
  return memory[n] 

for i in range(10):
  print(i,fibo(i+1),memory)