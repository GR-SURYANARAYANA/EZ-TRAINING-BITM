index = {'a':0,'b':1,'c':2,'d':3,'e':4,'f':5,'g':6,'h':7}
str = 'b1'
print(True if (index[str[0]] + int(str[1])) % 2 == 0  else False )
print(True if (ord(str[0]) + int(str[1])) % 2 == 1 else False )