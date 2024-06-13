import random

class Item:
    def __init__(self):
        self.item = {}
    def add_item(self,item_type,model_name,condition,status):
         while True:
             item_no = item_type[:2] + model_name[:2] + str(random.randint(1, 999))
             if str not in self.item:
                self.item[item_type] = {item_no:{'condition' : condition, status: status}}
             else:
                 self.item[item_type] += item_no: {'condition': condition, status: status}
        print("Admin you have successfully done with adding item ")