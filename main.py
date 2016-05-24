#main.py

def first_prompt():
    """Get top level key or list from the user

    >>>first_prompt('Thai'):
    This will prompt for the child Key

    >>>first_prompt('AFC'):
    This will prompt for the child Key

    >>>first_prompt('Romantic Comedy'):
    This will prompt for the child Key
    """


def second_prompt():
    """ prompt for child key

    >>>second_prompt('Yellow Curry'):
    'The following are ingredients in the {parent_key} dish {child_key}:\n• {items}'

    >>>second_prompt('West'):
    'The following are the teams in the {parent_key} {child_key}:\n• {items}'

    >>>second_prompt('The Princess Bride'):
    'The following actors are in {child_key} ({parent_key}):\n• {items}'

    """





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
