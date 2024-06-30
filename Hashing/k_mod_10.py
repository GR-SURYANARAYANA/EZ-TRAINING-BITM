class Node:
  def __init__(self,data) -> None:
    self.data = data
    self.next = None


class Hashing_KMod10:
  def __init__(self) -> None:
    self.hash_list = [None]*(10)
  
  get_key = lambda self,data : data %10

  def insert(self,data):
    if self.is_present(data):
      return
    key = self.get_key(data)
    if not self.hash_list[key]:
      self.hash_list[key] = Node(data)
      return 
    temp = self.hash_list[key]
    while temp.next:
      temp = temp.next
    temp.next = Node(data)
  
  def delete(self,data):
    key = self.get_key(data)
    if not self.is_present(data):
      return 'No match Found'
    else:
      temp = self.hash_list[key]
      previous = None
      while temp.data != data:
        previous = temp
        temp = temp.next
      if previous: 
          previous.next = temp.next
          temp.next = None
      else:
        self.hash_list[key] = None
      return 'Deleted sucessfully'
              

  def is_present(self,data):
    key = self.get_key(data)
    if not self.hash_list[key]:
      return False
    else:
      temp = self.hash_list[key]
      while temp.next and temp.data != data:
        temp = temp.next
      return (True if temp.data == data else False)
    
  def display(self):
      for i in range(len(self.hash_list)):
        print(i,':',end = " ")
        temp = self.hash_list[i]
        while temp:
            print(temp.data,end=" ")
            temp = temp.next
        print()

    
hashing =Hashing_KMod10()
while True:
   match input("1.Insert 2.Delete 3.Display 4.check present 5.Exit\nEnter your chocie : "):
      case '1': hashing.insert(int(input("Enter the value to insert : ")))
      case '2': print(hashing.delete(int(input("Enter the value to delete : "))))
      case '3':hashing.display()
      case '4':print(hashing.is_present(int(input("Enter the value to check : "))))
      case '5': break
      case _: print("invalid chocie ..!")
