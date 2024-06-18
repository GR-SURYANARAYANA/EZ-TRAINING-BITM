from library import LinkList
list = LinkList()
while True:
    match input('1.Insert Node at First 2.Insert Node at End 3.Display 4.Exit\nEnter yout choice : '):
        case '1': list.insert_at_first(input("Enter the value : "))
        case '2': list.insert_at_end(input("Enter the value : "))
        case '3': print(list)
        case _: break