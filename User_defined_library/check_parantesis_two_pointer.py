exp = input("Enter the expression :")

i = 0
j = len(exp) - 1

d = {'(': ')', '{': '}', '[': ']'}
count = 0
while i < j:
    if exp[i] == d[exp[j]]:
        i += 1
        j -= 1
    elif i < j and exp[i] in [')', '}', ']']:
        j -= 1
    else:
        i += 1
if i == j:
    print("valid expression")
else:
    print("invalid expression")