"""
Here goes the Student class with common thing and some extra property
"""


class Student(person):
    def __init__(self, first_name, last_name, unique_id):
        super().__init__(first_name, last_name, unique_id)
        self.taken_item = {}
