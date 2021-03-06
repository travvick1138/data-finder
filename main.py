# main.py

# import sys



import json

with open('data.json', 'r') as f:
    contents = f.read()
    data = json.loads(contents)

def search_list_item_and_return_parent_key_and_child_key(category, list_item):
    """find a ingredient and return parent and child keys

    """
    if list_item in data[category]["data"]:
        print(list_item)


def build_a_string(category):
    """Build strings for first_prompt and pulling in any data as needed

    >>>build_a_string("Food")
    'Enter the name of a cuisine ('Thai', 'Mexican', 'Italian', 'Indian') or an ingredient: '
    """
    value_list = list(data[category]["data"].keys())
    value_list.sort()

    return data[category]["strings"]['first_prompt'].format(
        parent_keys=', '.join(value_list)
    )

# def build_a_string(**kwargs):
#     if kwargs in data.keys():
#         category = kwargs
#         keys = data[category]["data"]
#         strings = data[category]["strings"]
#         value_list = list(keys.keys())
#         value_list.sort()
#
#         return strings['first_prompt'].format(
#             parent_keys=', '.join(value_list)
#         )
#
#     elif kwargs in data.keys():
#         (category, parent_key) = kwargs
#         keys = data[category]["data"]
#         strings = data[category]["strings"]
#         value_list = list(keys[parent_key].keys())
#         value_list.sort()
#         if parent_key not in keys.keys():
#             print("We do not have the information you are looking for, please try again.")
#             first_prompt(category)
#
#         return strings['second_prompt'].format(
#             child_keys=', '.join(value_list)
#         )
#
#
#     else:
#         kwargs not in data.keys()
#         print("We do not have the information you are looking for, please try again.")
#         main()

def first_prompt(key):
    user_input = input(build_a_string(key))


    second_prompt(key, user_input)

    return build_a_string(key)


def build_another_string(category, parent_key):
    """Build string for second_prompt and pulling any data as needed

    >>>build_another_string("Food", "Indian")
    'Enter the name of a dish ('Palak Paneer'): '
    """

    if parent_key in data[category].keys():
        value_list = list(data[category]["data"][parent_key].keys())
        value_list.sort()

        return data[category]["strings"]['second_prompt'].format(
            child_keys=', '.join(value_list)
        )
    elif parent_key not in data[category].keys():
        search_list_item_and_return_parent_key_and_child_key(category, parent_key)




def second_prompt(category, parent_key):
    user_input = input(build_another_string(category, parent_key))
    #user_input = input(build_a_string(category, parent_key))

    output(category, parent_key, user_input)

    return build_another_string(category, parent_key)
    #return build_a_string(category, parent_key)



def output(category, parent_key, child_key):
    """ list of ingredients for 2_inputs_outputs  """
    value_list = list(data[category]["data"][parent_key][child_key])
    value_list.sort()

    print(data[category]["strings"]['two_inputs_output'].format(
        parent_key=parent_key,
        child_key=child_key,
        items=('\n• '.join(value_list))
    ))

    final_prompt()

def final_prompt():
    # y = True
    while True:
        user_input = input("Would you like another search? (y or n)")
        if user_input == "y":
            main()
        else:
            break


def main():
    """ main gets the initial category imported from data:

    """
    keys = list(data.keys())
    keys.sort()
    import sys
    #while True:
    user_input = input('What category would you like to explore? ({data}): '.format(

        data=', '.join(keys)
    ))
    if user_input in keys:
        first_prompt(user_input)
    elif user_input not in keys:
        print("We do not have the information you are looking for, please try again.")
        main()
        # #else:
        #     None


main()
# if __name__ == '__main__':
#     import doctest
#
#     doctest.testmod()
