# main.py

import json

with open('data.json', 'r') as f:
    contents = f.read()
    data = json.loads(contents)

def build_a_string(category):
    """Build strings for each question pulling in any data as needed

    >>>build_a_string("Food")
    'Enter the name of a cuisine ('Thai', 'Mexican', 'Italian', 'Indian') or an ingredient: '
    """

    value_list = list(data[category]["data"].keys())
    value_list.sort()

    return data[category]["strings"]['first_prompt'].format(
        parent_keys=', '.join(value_list)
    )


def first_prompt(key):
    user_input = input(build_a_string(key))

    second_prompt(user_input)

    return build_a_string(key)


def second_prompt(parent_key):
    """ prompt for child key

    >>>second_prompt('Yellow Curry'):
    'The following are ingredients in the {parent_key} dish {child_key}:\n• {items}'

    >>>second_prompt('West'):
    'The following are the teams in the {parent_key} {child_key}:\n• {items}'

    >>>second_prompt('The Princess Bride'):
    'The following actors are in {child_key} ({parent_key}):\n• {items}'

    """


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
    #
    #
    # import json
    #
    # with open('data.json', 'r') as f:
    #     contents = f.read()
    #     data = json.loads(contents)

    for category in data.keys():
        keys = list(data.keys())
        keys.sort()

        user_input = input('What category would you like to explore? {data} '.format(

            data=', '.join(keys)
            ))

        first_prompt(user_input)
main()

if __name__ == '__main__':
    import doctest

    doctest.testmod()
