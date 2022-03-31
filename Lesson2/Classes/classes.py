

class Person:
    def __init__(self, name, age, city):
        self.name = name
        self.age = age
        self.city = city
    
    def get_name(self):
        print(self.name)
    
    def is_from_boston(self):
        return self.city == "Boston"