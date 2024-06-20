from library import LinkList
list = LinkList()
while True:
    match input('1.Insert Node at First 2.Insert Node at End 3.Insert at any position \n4.Delete at First 5.Delete at end 6.Detele At any point\n7.Display 8.Exit\nEnter yout choice : '):
        case '1': list.insert_at_first(input("Enter the value : "))
        case '2': list.insert_at_end(input("Enter the value : "))
        case '3': 
            data = input("Enter the vale : ")
            pos = int(input("Enter the postion : "))
            list.insert_at_any_postition(data,pos)
        case '4': list.delete_at_first()
        case '5': list.delete_at_last()
        case '6': list.delete_at_any_position(int(input("Enter the position : ")))
        case '7': print(list)
        case '8': break
        case _: print("Invalid Choice ")