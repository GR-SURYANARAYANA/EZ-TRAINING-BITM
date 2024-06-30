string = 'aeiou'

vowel = 0
for i in string:
  if i in 'aeiou':
    vowel+=1
print(vowel,len(string) -  vowel)

vowel = 0
for i in string:
  if i == 'a' or i == 'e' or i == 'o' or i == 'i' or i == 'u':
    vowel+=1
print(vowel,len(string) -  vowel)