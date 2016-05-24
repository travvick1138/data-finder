# main.py

def first_prompt(user_input):

    """Get top level key or list from the user

    >>>first_prompt('Food'):
    'Enter the name of a cuisine ('Thai', 'Mexican', 'Italian', 'Indian') or an ingredient: '

    >>>first_prompt('Football'):
    'Enter the name of a conference ('AFC', NFC) or team: '

    >>>first_prompt('Movies'):
    'Enter the name of a movie genre ('Action Thriller', 'Sci-Fi', 'Comedy', 'Romantic Comedy') or actor: '
    """
    import json

    with open('data.json', 'r') as f:
        contents = f.read()
        data = json.loads(contents)

    for first_prompt in data[user_input]['strings'].keys():
        parent_keys = data[user_input]['data'].keys()
        question = data[user_input]['strings']['first_prompt']

    user_input_1 = input('{question}'.format(

        question=question
    ))

    second_prompt(user_input_1, user_input)

def second_prompt(user_input, user_input_1):
    """ prompt for child key

    >>>second_prompt('Yellow Curry'):
    'The following are ingredients in the {parent_key} dish {child_key}:\n• {items}'

    >>>second_prompt('West'):
    'The following are the teams in the {parent_key} {child_key}:\n• {items}'

    >>>second_prompt('The Princess Bride'):
    'The following actors are in {child_key} ({parent_key}):\n• {items}'

    """

    import json

    with open('data.json', 'r') as f:
        contents = f.read()
        data = json.loads(contents)

    for second_prompt in data[user_input]['strings'][user_input_1].keys():
        child_keys = data[user_input]['data'][user_input_1]
        question = data[user_input]['strings']['second_prompt']

    user_input_2 = input('{question}'.format(

        question=question
    ))

def final_prompt(y, n):
    """for users to continue search

    >>>final_prompt(user_input):
    y = yes
    n = no
        user_input = input("Would you like another search? " ,y,n)

        if user_input == y:
            main()
        else:
            print("Goodbye")
               exit
               """


def main():

    """ main gets the initial category imported from data: """


    import json

    with open('data.json', 'r') as f:
        contents = f.read()
        data = json.loads(contents)

    for category in data.keys():
        keys = data.keys()

        user_input = input('What category would you like to explore? {data} '.format(

            data=', '.join(keys)
            ))

        first_prompt(user_input)
main()

if __name__ == '__main__':
    import doctest

    doctest.testmod()
