def tower(n,frm,to,aux):
  global ctr
  if n == 0:
    return
  tower(n-1,frm,aux,to)
  ctr+=1
  print(f'move {n} from {frm} to {to}')
  tower(n-1,frm,aux,to)

n = 2
ctr = 0
tower(n,'A','C','B')
print(ctr)