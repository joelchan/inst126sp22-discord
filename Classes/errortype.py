import json
from os import path


class ErrorType:

    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.image = self.getImage()

    def getImage(self):
        file = f'assets/{self.name}.png'
        if path.exists(file):
            return file
        else:
            return None

def __fetchErrors__():
    errors = []
    f = open('assets/errors.json')
    data = json.load(f)
    for item in data['errors']:
        errors.append(ErrorType(item['name'], item['description']))
    return errors

errors = __fetchErrors__()