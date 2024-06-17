def getAmstrong(n, digit):
    sum = 0
    while n > 0:
        sum += ((n % 10) ** digit)
        n /= 10
    print(sum)
    return sum


def getDigit(num):
    count = 0
    while num > 0:
        count += 1
        num = num / 10
    print(int(count))
    return int(count)


n = 143
result = getAmstrong(n, getDigit(n))
print(result)
