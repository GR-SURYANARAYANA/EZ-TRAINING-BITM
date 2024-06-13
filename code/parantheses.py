s = "(("
ls = []
count = 0
d = {'(': ')','[' : ']','{' : '}'}
for i in s:
  if i in ['(','[','{']:
    ls.append(i)
    print(i,ls)
  elif i in [')',']','}']:
    if ls and ls.pop() == d[i]:
      print(i,ls)
    else:
      print("failed")
      break
print("pass")