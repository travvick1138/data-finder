#main.py

import json

with open ('data.json', 'r') as f:
    contents = f.read()
    data = json.loads(contents)

def main():

    for category in main.keys():
        print(main[category])
    user_input = input('What category would you like to explore')
