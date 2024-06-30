import math
def reverse_number(n):
  return int(str(n)[::-1])

n = int(input(""))
total_digit = int(math.log10(n))+1
half_digit = math.floor(total_digit/2)
first_part = n // (10**half_digit)
second_part = reverse_number(n % (10**(half_digit)))
print(n,':',first_part,'+',second_part,'=',first_part+second_part)


# print("surya"[::-2])