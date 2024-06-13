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