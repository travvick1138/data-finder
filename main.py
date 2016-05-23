#main.py





def main():
    import json

    with open ('data.json', 'r') as f:
        contents = f.read()
        data = json.loads(contents)

#    data = json.loads(contents)
    user_input = input('What category would you like to explore? ')
    for category in data.keys():
        print(data[category])
main()
