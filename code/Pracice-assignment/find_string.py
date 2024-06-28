
s = 'ABABABCANFKABABCNKABABCACNDA'
p = 'ABABCA'


index = []
i = 0
count = 0
j = 0
while i <len(s):
  count +=1
  if s[i] == p[j]:
    j+=1
    i+=1
    if j == len(p):
      index.append(i-len(p))
      j = 0
  else:
    i = i - j + 1
    j = 0

print(index)
# while i<len(s):
#   if s[i:i+len(p)] == p:
#     index.append(i)
#   i+=1
# i = 0
# ls = re.findall(p,s)
# print(ls)
# j = 0
# p = 'ooo'
# s = 'Ghoorpade is a goood booy...booy'
# import re