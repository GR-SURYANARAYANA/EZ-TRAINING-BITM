def operation(a, b, op):
    match op:
        case '*':
            return a * b
        case '//':
            return a // b
        case '**':
            return a ** b
        case '/':
            return a / b
        case '+':
            return a + b
        case '-':
            return a - b
        case _:
            return None


value = input()
length = 0
i = 0
for i in range(len(value)):
    if (value[i] + value[i + 1]) in ['//', '**']:
        op = value[i] + value[i + 1]
        length = 2
        break
    if value[i] in ['*', '+', '/', '%']:
        length = 1
        break
a = float(value[0:i])
op = value[i:i + length]
b = float(value[i+length:])
print(operation(a, b, op))
