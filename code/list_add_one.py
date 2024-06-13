def plusOne(digits):
        i = len(digits) - 1
        carry = 1
        while i >= 0:
            sum = digits[i] + carry
            digits[i] = sum % 10
            carry = (1 if sum > 9 else 0)
            print(carry)
            i -= 1
        if carry == 1:
            digits = [carry] + digits
        return digits
            
print(plusOne([9]))