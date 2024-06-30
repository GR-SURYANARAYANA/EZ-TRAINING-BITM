ls = [None]*10
key = lambda data : data % 10
while True:
   match input("1.Insert 2.Delete 3.Display 5.Exit\nEnter your chocie : "):
      case '1':
          num = int(input("Enter the number to insert : "))
          h = key(num)
          if not ls[h] or ls[h] == '*':
             ls[h] = num 
          else:
              temp = (h + 1) % 10
              while temp != h:
                if not ls[temp] or ls[temp] == '*':
                  ls[temp] = num
                  break
                temp = (temp + 1) % 10
              print({f'Inserted at {temp}' if temp != h else 'Hash Table is full'})
      case '2':
          num = int(input("Enter the number to delete : "))
          h = key(num)
          temp = h + 1
          while temp != h:
            if not ls[temp]:
              break
            elif ls[temp] == num:
               ls[temp] = '*'
               break
            temp = (temp + 1) % 10
          print({f'Deleted at {temp}' if ls[temp] == '*' else 'No element found'})  
      case '3':
         print(ls)
      case '5': break
      case _: print("invalid chocie ..!")
