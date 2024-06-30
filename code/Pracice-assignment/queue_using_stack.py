class Stack:

    def __init__(self):
        self.__items = []

    def push(self, ele):
        self.__items.append(ele)

    def pop(self):
        return self.__items.pop() if len(self) > 0 else None

    def peek(self):
        return self.__items[-1]

    def isempty(self):
        return False if self.__items else True

    def make_empty(self):
        self.__items.clear()

    def __len__(self):
        return len(self.__items)
    
    def __str__(self):
        return f'{self.__items[::-1]}'
    

class Queue:
  def __init__(self) -> None:
    self.stack = Stack()
  

  def enqueue(self,ele):
    if not self.stack:
      return self.stack.push(ele)
    previous = self.stack.pop()
    self.enqueue(ele)
    self.stack.push(previous)
  
  def dequeue(self):
    return self.stack.pop()
  
  def __len__(self):
    return self.stack.__len__()
  
  def __str__(self):
    return f'{self.stack}'
  
queue = Queue()
while True:
   match input("1.Enqueue 2.Dequeue 3.Display 4.Exit\nEnter your chocie : "):
      case '1': queue.enqueue(int(input("Enter the value to insert : ")))
      case '2': print(queue.dequeue())
      case '3 ':print(queue)
      case '4 ': break
      case '5': print("invalid chocie ..!")

