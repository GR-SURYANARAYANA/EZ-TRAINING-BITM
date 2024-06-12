import random

admins = {}
students = {}
"""
Class of person where it is common for both of them
"""
class __Person__:
    def __init__(self, first_name, last_name, unique_id):
        self.__unique_id__ = unique_id
        self.__first_name__ = first_name
        self.__last_name__ = last_name

    def __str__(self):
        return (f"First Name : {self.__first_name__} "
                f"Last Name  : {self.__last_name__}"
                f"Unique Id  :  {self.__unique_id__}")


class Item:
    def __init__(self):
        self.item = {}
    def add_item(self,item_type = None,model = Nonw):
         while True:
             str = item_type[:2] + model[:2] + str(random.randint(1, 999))
             if str not in self.item:
                 self.item[str] = {"type" : item_type , "model" : model, "available":True }break

        print("Admin you have successfully done with adding item ")



"""
Here goes the Student class with common thing and some extra property
"""
class Student(__Person__):
    def __init__(self, first_name, last_name, unique_id):
        super().__init__(first_name, last_name, unique_id)
        self.taken_item = {}

class Admin(__Person__):
    def __init__(self, first_name, last_name, unique_id):
        super().__init__(first_name, last_name, unique_id)

    def




