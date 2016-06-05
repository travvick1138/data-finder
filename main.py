# main.py

# __test__
# """Build strings for first_prompt and pulling in any data as needed
#
#    >>>build_a_string("Food")
#    'Enter the name of a cuisine ('Thai', 'Mexican', 'Italian', 'Indian') or an ingredient: '
#    """



# import json
#
# with open('data.json', 'r') as f:
#     contents = f.read()
#     data = json.loads(contents)
#
# def search_list_item_and_return_parent_key_and_child_key(key, ingredient):#find a ingredient and return parent and child keys
#
#     # for ingredient in key:
#     #     for parent_key in data.keys():
#     #         for child_key in data["data"][parent_key]:
#     #             if ingredient in key[data][parent_key][child_key]:
#     #                     print(key["strings"]['one_input_output'].format(
#     #                         parent_keys=parent_key,
#     #                         child_key=child_key,
#     #                         ingredient=', '.join(ingredient)
#     #                     ))
#     #              else:
#     #                  print("We do not have the item you are looking for. Please try again")
#     #                  first_prompt(category)
#                  #print(parent_key, child_key, list_item)
#
#
#
#
# def build_a_string(category):
#
#     value_list = list(data[category]["data"].keys())
#     value_list.sort()
#
#     return data[category]["strings"]['first_prompt'].format(
#         parent_keys=', '.join(value_list)
#     )
#
# # def build_a_string(data, **kwargs):
# #     if kwargs in data.keys():
# #         category = kwargs
# #         keys = data[category]["data"]
# #         strings = data[category]["strings"]
# #         value_list = list(keys.keys())
# #         value_list.sort()
# #
# #         return strings['first_prompt'].format(
# #             parent_keys=', '.join(value_list)
# #         )
# #
# #     elif kwargs in data.keys():
# #         (category, parent_key) = kwargs
# #         keys = data[category]["data"]
# #         strings = data[category]["strings"]
# #         value_list = list(keys[parent_key].keys())
# #         value_list.sort()
# #         if parent_key not in keys.keys():
# #             print("We do not have the information you are looking for, please try again.")
# #             first_prompt(category)
# #
# #         return strings['second_prompt'].format(
# #             child_keys=', '.join(value_list)
# #         )
# #
# #
# #     else:
# #         kwargs not in data.keys()
# #         print("We do not have the information you are looking for, please try again.")
# #         main()
#
# def first_prompt(key):
#     user_input = input(build_a_string(key))
#
#     second_prompt(key, user_input)
#     # if user_input not in data[key]:
#     #         list_item = search_list_item_and_return_parent_key_and_child_key(key, user_input)
#     #         print(key["strings"]['one_input_output'].format(
#     #                              list_item=list_item,
#     #                              parent_key=parent_key,
#     #                              child_key=child_key
#     #                          ))
#
#
#
#     return build_a_string(key)
#
#
# def build_another_string(category, parent_key):
#     """Build string for second_prompt and pulling any data as needed
#
#     >>>build_another_string("Food", "Indian")
#     'Enter the name of a dish ('Palak Paneer'): '
#     """
#
#     if parent_key in data[category].keys():
#         value_list = list(data[category]["data"][parent_key].keys())
#         value_list.sort()
#
#         return data[category]["strings"]['second_prompt'].format(
#             child_keys=', '.join(value_list)
#         )
#     elif parent_key not in data[category].keys():
#             search_list_item_and_return_parent_key_and_child_key(category, parent_key)
#
#
# def second_prompt(category, parent_key):
#     user_input = input(build_another_string(category, parent_key))
#     #user_input = input(build_a_string(category, parent_key))
#
#     output(category, parent_key, user_input)
#
#     return build_another_string(category, parent_key)
#     #return build_a_string(category, parent_key)
#
#
#
# def output(category, parent_key, child_key):#list of ingredients for 2_inputs_outputs
#
#     value_list = list(data[category]["data"][parent_key][child_key])
#     value_list.sort()
#
#     print(data[category]["strings"]['two_inputs_output'].format(
#         parent_key=parent_key,
#         child_key=child_key,
#         items=('\n• '.join(value_list))
#     ))
#
#     final_prompt()
#
# def final_prompt():# for users to continued
#
#     while True:
#         user_input = input("Would you like another search? (y or n)")
#         if user_input == "n":
#             exit()
#         elif user_input == "y":
#             return main()


def get_parent_key_or_ingredient(dataset, strings):
    """Pass along the primary key choices and give the opportunity to choose and ingredient

    """
    value_list = list(dataset)
    value_list.sort()

    return strings["first_prompt"].format(
             parent_keys=', '.join(value_list))

def search_for_list_item_and_return_parent_keys_and_child_keys(dataset, strings, item):
    """Return a list item ot return the user to the previous prompt

    """
    if item == "":
        print("By pressing return without an answer you have chosen to quit. Goodbye!")
        return None, None
    while True:
        try:
            tuple_list = []
            for parent_key in dataset:
                for child_key in dataset[parent_key]:
                    if item not in dataset[parent_key][child_key]:
                        print("We do not have the information you are looking for, please try again.")
                        main()

                    elif item in dataset[parent_key][child_key]:
                        tuple_list.append((parent_key, child_key))
                        tuple_list.sort()
                        string_list = ""
                        for match in tuple_list:
                            string_list += strings["one_input_output"].format(
                                                                list_item=item,
                                                                parent_key=match[0],
                                                                child_key=match[1]
                                                                 ) + '\n'
                        return print(string_list)
        except ValueError:
            print("We do not have the information you are looking for, please try again.")
            get_parent_key_or_ingredient(dataset, strings)


def get_child_key_from_parent_key(dataset1, strings):
    """Return request for child key

    """
    value_list = list(dataset1)
    value_list.sort()

    return(strings["second_prompt"].format(
            child_keys=(', '.join(value_list))
        ))

def output(dataset2, strings):#list of ingredients for 2_inputs_outputs

    value_list = list(dataset2)
    value_list.sort()

    print(strings['two_inputs_output'].format(
        parent_key=dataset2[0],
        child_key=dataset2[1],
        items=('\n• '.join(value_list))
    ))

    quit()

def quit():
    quit_input = input("would you like to try again? (y/n) \n")
    if quit_input == "n":
        print("Thank you, Goodbye!")
        return None, None
    else:
        main()


def main():
    """ main controls the flow of the program:

    """
    import json

    with open('data.json', 'r') as f:
        contents = f.read()
        data = json.loads(contents)
        keys = list(data.keys())
        keys.sort()

    user_input = input('What category would you like to explore? ({data}): '.format(

        data=', '.join(keys)
    ))

    if user_input == "":
        print("By pressing return without an answer you have chosen to quit. Goodbye!")
        return None, None
    elif user_input not in keys:
        print("We do not have the information you are looking for, please try again.")
        main()

    dataset = data[user_input]["data"]
    strings = data[user_input]["strings"]

    parent_key = input(get_parent_key_or_ingredient(dataset, strings))
    if parent_key not in dataset:
        bool(search_for_list_item_and_return_parent_keys_and_child_keys(dataset, strings, parent_key))
        quit()
    elif parent_key in dataset:
        dataset1 = dataset[parent_key]
        child_key = input(get_child_key_from_parent_key(dataset1, strings))
        if child_key == "":
            print("By pressing return without an answer you have chosen to quit. Goodbye!")
            return None, None
        elif child_key not in dataset[parent_key]:
            print("We do not have the information you are looking for, please try again.")
            get_child_key_from_parent_key(dataset1, strings)
        else:
            dataset2 = dataset1[child_key]
            output(dataset2, strings)

main()
# if __name__ == '__main__':
#     import doctest
#
#     doctest.testmod()
