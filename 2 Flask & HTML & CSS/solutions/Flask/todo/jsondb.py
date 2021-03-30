


import json

class JsonDB:
    def __init__(self, path):
        self.path = path
        self.data = None
    
    def load(self):
        with open(self.path, 'r') as file:
            contents = file.read()
        self.data = json.loads(contents)
    
    def save(self):
        with open(self.path, 'w') as file:
            file.write(json.dumps(self.data, indent=4))
    






