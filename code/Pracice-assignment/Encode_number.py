"""
11) Encode The Number
You work in the message encoding department of a national security agency. Every message
that is sent from or received in your office is encoded. You have an integer N, and each digit
of N is squared and the squares are concatenated together to encode the original number.

Your task is to find and return an integer value representing the encoded value of the
number.
input1: An integer value N representing the number to be encoded.

Output :
Return an integer value representing the encoded value of the number.

Sample Input:
167

Sample Output:
13649 
"""
import math
def get_digit(n):
  return int(math.log10(n) + 1)

n = int(input())

# digit = get_digit(n)
# # result = 0
# # while digit!= 0:
# #   result = n // (10**digit)
# #   square = result * result
# #   square_digit = get_digit(square)
# #   result = result * (10**square_digit) + square
# #   digit -= 1
# print(result)

# while n != 0:




