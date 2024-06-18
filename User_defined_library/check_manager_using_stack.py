from library import Stack

ls = [3, 5, 2, 14, 5, 3, 7, 9, 4, 6, 9, 4, 2, 5, 3]
print(ls)
stack = Stack()
for i in range(len(ls) - 1, -1, -1):
    if not(stack.isempty()):
        while not(stack.isempty()) and stack.peek() <= ls[i]:
            stack.pop()
    if stack.isempty():
        ls[i] = -1
    else:
        ls[i] = stack.peek()
    stack.push(i)
print(ls)
