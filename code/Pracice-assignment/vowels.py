n = int(input("Enter the number of people : "))
ls = [input().split(",") for i in range(n)]
vowels = ['a','e','i','o','u']
result = {}
for person in ls:
  count = []
  for char in vowels:  
    count.append(person[1].count(char.upper()) + person[1].count(char))
  get_max = max(count)
  result[person[0]] = [vowels[i] for i in range(len(count)) if get_max == count[i]]
print(result)
          
          
  # d = {person[0] : [vowels[i] for i in range(len(count)) if get_max == count[i]]}
  # result.append(d)
  # for i in range(len(count)):
  #   if get_max == count[i]:
  #     d[person[0]] = d[person[0]] + [vowels[i]]
     

    
