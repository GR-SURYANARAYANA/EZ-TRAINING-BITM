date = int(input())
car_list = map(int,input().split(" "))
is_even_date = (date % 2 == 0)

# date - odd        even car
# date- even        odd car 

fine = 0
for i in car_list:
  is_car_odd = (i % 2 == 1)
  if is_even_date and is_car_odd:
    fine+=250
  elif not is_even_date and not is_car_odd:
    fine+=250

print(fine)
