import requests

class APIClient:
    def __init__(self, username, api_key):
        self.username = username
        self.API_key = api_key
        self.endpoint = "https://api.github.com/zen"
    
    def get_value_from_api(self, value):
        return requests.get(self.endpoint".....")

class Person:
    def __init__(self, name, age, city):
        self.name = name
        self.age = age
        self.city = city
    
    def get_name(self):
        print(self.name)
    
    def get_age(self):
        return self.age
    
    def is_from_boston(self):
        return self.city == "Boston"