from mcutils import *

credits = Credits(authors = ['Matias Canepa Gonzalez'], team_name= 'Ditto Team',github_account='http://github.com/macanepa',
                  email_address='macanepa@miuandes.cl',company_name='AChiliMountain')


def print_data(*args):
    print "Excecuting Function:"
    print "print_data"
    print args

func1 = Menu_Func(print_data,"Function 1",*(1,2,3,9,8,7))
m1_exit = Menu_Func(exit_application,"Exit","Exiting Application!")
m1_credits = Menu_Func(credits.print_credits,title="Credits")

menu3 = Menu("MENU 3","subtitle ijiofjeoi","select option wiwiiii",[func1,"WIWI","WAWA"],return_type=int)
menu2 = Menu("MENU 2", "subtitle", "select option", [menu3], return_type=int)
menu1 = Menu("MAIN MENU",options=[func1,menu2,m1_credits,m1_exit],return_type=int,back=False)

while True:
    op = menu1.print_menu()