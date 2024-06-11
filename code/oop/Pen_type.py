class Pen:
  def __init__(self,company):
    print(f"Hi {company}...! Welcome to new design phase ")
  
  def make_product(self,items,length,breadth):
      self.item = items
      self.length = length
      self.breadth = breadth
      print("Length of item: ",length)
      print("Breadth of item : ",breadth)
  
  def find_cost(self,cost_per_unit):
     self.per_unit = cost_per_unit
     print("Overall cost to produce : ",self.length*self.breadth * cost_per_unit *self.item)
  
dom = Pen("DOOMS Prodcuction")
dom.make_product(20,10,3)
dom.find_cost(5)