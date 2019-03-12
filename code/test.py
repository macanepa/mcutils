from mcutils import *

def sqrt(x):
    #x = int(raw_input("Select Number: "))**.5
    x=int(x)
    x**=.5
    print x
    return x



sqrt_menu_func = Menu_Func(sqrt,"Calculate Sqrt of 9",*["9"])
exit_menu_func = Menu_Func(exit_application,"what",*["Exiting Application"])

sub_menu_lvl2 = Menu(title="Submenu Lvl 2", text="Hello! You've Reached level 2! Choose one option below",
                     options=["wiwi","wawa",exit_menu_func])

sub_menu_lvl1 = Menu(title="Submenu Lvl 1",text="Choose one number",options=[1,2,sub_menu_lvl2])
main_menu = Menu(title = "Main Menu",text="Select an Operation", options = [sqrt_menu_func,sub_menu_lvl1,"Option 3"],back=False)

while True:
    main_menu.show()