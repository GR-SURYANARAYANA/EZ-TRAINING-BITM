result = []
def permutation(string,answer):
  global result
  if not string:
    return result.append(answer)
  for i in range(len(answer) + 1):
    if not answer:
      permutation(string[1:],string[0])
    else:  
      permutation(string[1:],answer[:i] + string[0] + answer[i:])


permutation("abcd","")
print(result)