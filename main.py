# main.py

def first_prompt(parent_keys):

    """Get top level key or list from the user

    >>>first_prompt('Thai'):
    This will prompt for the child Key

    >>>first_prompt('AFC'):
    This will prompt for the child Key

    >>>first_prompt('Romantic Comedy'):
    This will prompt for the child Key
    """


def second_prompt(child_keys):
    """ prompt for child key

    >>>second_prompt('Yellow Curry'):
    'The following are ingredients in the {parent_key} dish {child_key}:\n• {items}'

    >>>second_prompt('West'):
    'The following are the teams in the {parent_key} {child_key}:\n• {items}'

    >>>second_prompt('The Princess Bride'):
    'The following actors are in {child_key} ({parent_key}):\n• {items}'

    """


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
        user_input = input('What category would you like to explore? {data}'.format(

            data=keys
            ))

main()

if __name__ == '__main__':
    import doctest

    doctest.testmod()
