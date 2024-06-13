class IA:
  def __init__(self,student = "None",subject = 5):
    print(f"Enter marks for student of usn : {student}")
    self.__IA = [self.__get_marks_from_console(i+1) for i in range(subject)]
    self.__calculate_percentage()

  def __get_marks_from_console(self,n):
    return int(input(f"Enter the marks of internal {n} : "))
  
  
  def __calculate_percentage(self):
    self.__percentage = sum(self.__IA) / len(self.__IA)
    self.__grade = self.__cal_grade()
  
  
  def __cal_grade(self):
    grade = {10: 'O',9 :'O',8:'A+',7:'A',6:'B+',5:'C+',4:'C',3:'F',2:'F',1:'F',0:'F'}
    return grade[self.__percentage // 10]
  def __print_marks(self):
    str = [f"Subject {i+1} : {self.__IA[i]}" for i in range(len(self.__IA))]
    return "\n".join(str)

  def __str__(self):
    return str.format(f"""Marks-Obtained Details 
{self.__print_marks()}
percentage : {self.__percentage}
grade : {self.__grade}
""")
    

class Student:
  def __init__(self,name):
    print("Enter the student Details below : ")
    self.__name = input("Enter the name : ")
    self.__IA = IA(name)
  
  def __str__(self) -> str:
    return str.format(f"""Name : {self.__name}
{self.__IA}""")

# MAin starts

dict = {}
def add_student():
  while True:
      usn = input("Enter the usn Of the student : ")
      if usn not in dict:
          student = Student(usn)
          dict[usn] = student
          break
      else:
          print("Student already existed...!Try Unique Number :")

def display_student():
  while True:
      usn = input("Enter the usn Of the student : ")
      if usn not in dict:
          print("Student Not existed In list...!Try Valid Student USN :")
      else:
         print(dict[usn])
         break

def remove_student():
   while True:
      usn = input("Enter the usn Of the student : ")
      if usn in dict:
         dict.pop(usn)
         print("{usn} has been sucessully deleted")          
      else:
         print("Student doesn't exist in the list")
         break
   


while True:
  while True:
    ch = input("1.ADD Student 2.Remove_Student 3.Display_Student 4.Exit \nEnter the choice : ")
    match ch:
      case '1':
          add_student()
      case 2:
          remove_student()
      case '3':
          display_student()
      case '4':
          exit(0)    
      case '_' :
          print("Invalid student ")
          

