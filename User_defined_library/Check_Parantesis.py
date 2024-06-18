import library

stack = library.Stack()

exp = input("Enter the expression :")

d = {'(': ')', '{': '}', '[': ']'}
flag = True
for i in exp:
    if i in ['(', '{', '[']:
        stack.push(i)
    if i in [')', '}', ']']:
        if len(stack) > 0:
            if d[stack.peek()] == i:
                stack.pop()
                continue
            else:
                flag = False
                break
print('Valid Expression' if flag and stack.isempty() else 'invalid Expression')
