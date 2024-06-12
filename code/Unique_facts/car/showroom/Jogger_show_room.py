import company
class Showroom:
  def __init__(self,model = ['Ferrari','Toyato','Range-Rover']) -> None:
    self.model = model

  def car_company(self,name = "Customer"):
    print("*******************************************")
    print(f"Welcome {name} ")
    print("*******************************************")
    while True:
      print("Here are some list of Branded car That can you look : ")
      for i in self.model:
        print(i)
      while True:
         brand = input("Enter the name of brand that you want to visit : ")
         if brand in self.model():
           break
      match brand:
        case 'Ferrari': comapny.Ferrari() 
        case 'Toyato'  : company.Toyoto()
        case 'Range-Rover': company.Range_Rover() 
        case _:print("Invalid choice has been made Please Try again later : ")

      


