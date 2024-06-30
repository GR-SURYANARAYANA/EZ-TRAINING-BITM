import math


def digit_product(num):
  if num == 0:
    return 1
  return (num%10) * digit_product(num//10)

def sum_of_digit(num):
  if num:
    return (num%10) +  sum_of_digit(num//10)
  return 0

def reverse_number(num):
  if num == 0:
    return 0
  return (num%10) * (10 ** int(math.log10(num)))  + reverse_number(num//10) 

def is_palindrome(num):
  if num < 10:
    return True
  
  last_digit = num % 10
  num = num // 10
  first_digit = num // (10**int(math.log10(num)))
  if last_digit != first_digit:
    return False
  return is_palindrome(num - first_digit * int(10**math.log10(num)) )
  
def zeros_count(num):
  if num == 0:
    return 0
  return zeros_count(num//10) + (1 if num%10 == 0 else 0) 

num = int(input("Enter the number : "))
print(zeros_count(num)) 
