import requests

class APIClient:
    def __init__(self, username, api_key):
        self.username = username
        self.api_key = api_key
    
    def get_states(self, state_name):
        requests.get("/us/states" + state_name, {"headers":{"api_key": self.api_key}})