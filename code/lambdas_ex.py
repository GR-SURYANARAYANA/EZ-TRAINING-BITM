# a = lambda a:"Odd" if a%2 else "Even"
is_vowel = lambda x:True if x in ['a','e','i','o','u'] else False
a = lambda a,b: True if is_vowel(a) and is_vowel(b) else False

print(a("surya","chandra"))