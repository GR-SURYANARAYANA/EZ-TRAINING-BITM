s = "egg"
t = "add"
d = {}
for i in range(len(s)):
  if s[i] not in d:
    d[s[i]] = t[i]
  else:
    if d[s[i]] == t[i]:
      continue
    else:
      print(False)
      break
print(t)
  # print(s[i],t[i])
