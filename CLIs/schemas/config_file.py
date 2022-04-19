import yaml 
from pathlib import Path

class ConfigFile:
    def __init__(self, file_location=None,input_data=None) -> None:
        self.file_location = file_location
        self.data = self.load_data()
        self.input_data = input_data
    
    def load_data(self) -> dict:
        try:
            with open(self.file_location, 'w') as file:
                documents = yaml.dump(self.input_data, file)
        except FileNotFoundError:
            print("File not found")
        return documents
