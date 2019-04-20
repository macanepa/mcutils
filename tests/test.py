import mcutils as mc
import os



def validation(input_string):
    print(input_string.isnumeric())
    if(input_string.isnumeric()):
        value = int(input_string)
        print(value)
        return True
    return False

# value = mc.get_input(text="Name",validation_function=validation)

# TODO: Fix broken checker
main_menu = mc.Menu(title="Main Menu",options=[1,2,3],back=False)

while True:
    main_menu.show()

# list_a = ["Name","Last_Name","Age"]
# dict_a = dict.fromkeys(list_a)
# print(list_a)
# print(dict_a)
