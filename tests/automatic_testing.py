import mcutils as mc
mc.activate_mc_logger()
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
    mc.ColorSettings.is_dev = False
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


mc.mcprint(text='text', color=mc.Color.RED)
menu_testing()
menu_select_options()
