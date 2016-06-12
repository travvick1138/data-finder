""" This is our second build of the data-finder project started by Travis and Jeff
on 5.23.16. main2.py will have a larger main function to transform data and return it to the main function for processing. """


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
    list_item = item

    if item == "":
        print("By pressing return without an answer you have chosen to quit. Goodbye!")
        return None, None
    # while True:
    #     try:
    #         tuple_list = []
    for parent_key in dataset:
        for child_key in dataset[parent_key]:
            try:
        # If `.index` succeeds, it returns a number between 0 and the index of the last item in the list
        # If it fails, it throws a ValueError
                if dataset[parent_key][child_key].index(list_item) > -1:
                    print(strings['one_input_output'].format(
                        list_item=list_item,
                        parent_key=parent_key,
                        child_key=child_key
                    ))
                 # Return results as a tuple
            except ValueError:
                continue
    quit()

        #             if item not in dataset[parent_key][child_key]:
        #                 print("We do not have the information you are looking for, please try again.")
        #                 main()
        #
        #             elif item in dataset[parent_key][child_key]:
        #                 tuple_list.append((parent_key, child_key))
        #                 tuple_list.sort()
        #                 string_list = ""
        #                 for match in tuple_list:
        #                     string_list += strings["one_input_output"].format(
        #                                                         list_item=item,
        #                                                         parent_key=match[0],
        #                                                         child_key=match[1]
        #                                                          ) + '\n'
        #                 return print(string_list)
        # except ValueError:
        #     print("We do not have the information you are looking for, please try again.")
        #     get_parent_key_or_ingredient(dataset, strings)
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
