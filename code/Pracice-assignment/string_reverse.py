def strrev(str,i):
  if i==len(str):
    return ""
  return strrev(str,i+1) + str[i] 


print(strrev("surya",0))