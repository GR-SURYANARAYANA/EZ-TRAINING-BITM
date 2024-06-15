import math


def sum(gates,start,end):
  sum = 0 
  for i in range(start,end):
    sum += gates[i]
  return sum

def check_equilibrium(gate):
  for i in range(1,len(gate)):
    if (sum(gate,0,i) - sum(gate,i,len(gate))) == 0:
      return i
  return -1

gates = [list(map(int,input().split(" "))) for i in range(7)]
result = {}
count = 0
for gate in gates:
  temp = check_equilibrium(gate)
  check = (temp if  temp >= 0 else math.ceil((len(gate)-1)/2))
  equilibrium = (f'#equilibrum index {check}' if temp >= 0 else f'#No Equilibrium status {check}')
  count= count + 1
  result[f'checkpoint {count}'] = equilibrium 
print(result)

"""
1 2 1 1 1
1 4 3 2 3
2 2 3 4 1
1 3 2 2 0
1 4 2 3 1
3 0 3
1 1 1 1 1
"""