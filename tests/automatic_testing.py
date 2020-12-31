import mcutils as mc
import logging
mc.activate_mc_logger(console_log_level='info')
mc.ColorSettings.is_dev = True

"""
Automatic testing for mcutils
"""


def menu_testing():
    def exp(num, exp_):
        num = num ** exp_
        print(num)
        return num

    credits_ = mc.About(authors=['Matías Cánepa'],
                        company_name='ALM',
                        github_account='macanepa',
                        github_repo='https://github.com/macanepa/logistics-solver')

    mf_credits = mc.MenuFunction(title='Credits', function=credits_.print_credits)
    mf_sqrt = mc.MenuFunction(title='SQRT', function=exp, exp_=4, num=3)
    mc_main = mc.Menu(title='Main Menu', options=[mf_sqrt, mf_credits])

    mc_main.show()


def validation():
    number = mc.get_input(text='input a value greater than 5, different than 10',
                          valid_options=['!=10', '>5'],
                          return_type=int)
    mc.mcprint(text='input value = {}'.format(number),
               color=mc.Color.LIGHTGREEN)


mc.ColorSettings.is_dev = False
mc.ColorSettings.print_color = True


def menu_select_options():
    mc.ColorSettings.is_dev = True
    mc.ColorSettings.print_color = True
    #  options = ["Animal", "Wiweño", "Shalashaska Ocelot"]
    options_classy = {"Animal": [str, '<10', '>3'],
                      "Edad":   [int, '>0', '<=100']}
    mc_main = mc.Menu(title="Testing Selection",
                      subtitle='Please input all fields',
                      options=options_classy,
                      input_each=True)

    mc_main.show()
    print(mc_main.returned_value)
    print(mc_main.function_returned_value)

def function():
    def return_name(n):
        name = mc.get_input(text=f'This is just the param: {n}')
        return name

    mf_return_name = mc.MenuFunction(title='Return Name', function=return_name, n=2)
    mc_menu = mc.Menu(title='Function Testing',
                      subtitle='Select an option from below',
                      text='This is the text',
                      options=[mf_return_name])

    mc_menu.show()
    print(f'function returner value: {mc_menu.function_returned_value}')
    print(f'menu returned value {mc_menu.returned_value}')

    mc_input_each = mc.Menu(title='Input Each',
                            options={'Name': [str, '>5']},
                            input_each=True)
    mc_input_each.show()
    # logging.info(f'Input was {mc_input_each.returned_value}')
# mc.mcprint(text='text', color=mc.Color.RED)
# menu_testing()
# menu_select_options()
# function()

# mc.date_generator(True)

import mcutils as mc
def foo(n):
    return n**2
mf_foo = mc.MenuFunction(title='do foo', function=foo, n=4)
mc_submenu = mc.Menu(title='Submenu',
                     text='This is the submenu',
                     options=[mf_foo])
mc_menu = mc.Menu(title='Main Menu',
                  subtitle='Subtitle',
                  text='Please select one of the following options',
                  options=[mc_submenu, 'Option 2', 'Option 3'])
mc_menu.show()
print(mc_submenu.function_returned_value)
