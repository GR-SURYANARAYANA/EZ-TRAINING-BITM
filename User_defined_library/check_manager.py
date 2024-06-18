# ls = [3, 5, 2, 14, 5, 3, 7, 9, 4, 6, 9, 4, 2, 5, 3
ls = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(ls, len(ls))


def find_max(ls, ele, start):
    for i in range(start, len(ls)):
        if ele < ls[i] and ele != ls[i]:
            return i
    return -1


i = 0

while i != len(ls):
    max_index = find_max(ls, ls[i], i + 1)
    if max_index > i:
        ls[i:max_index] = [ls[max_index]] * (max_index - i)
        i = max_index
    else:
        ls[i] = -1
        i += 1
print(ls, len(ls))
