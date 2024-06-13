import os
# str = []
# with open("demo.txt","r") as file:
#   for i in file.readlines():
#     str.append(i)
#   file.close()
# with open("demo.txt","w") as file:
#   for i in range(len(str)):
#     str[i] = str[i].replace("Bellary","BITM")
#     print(str[i])
#   str = "".join(str)
#   file.write(str)
#   file.close()

with open("demo.txt","r+b") as file:
  file.seek(-34,2)
  file.write(b'surya')
  file.close()
