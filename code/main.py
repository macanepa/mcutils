from mcutils import *

credits = Credits(authors = ['Matias Canepa Gonzalez'], team_name= 'Ditto Team',github_account='http://github.com/macanepa',
                  email_address='macanepa@miuandes.cl',company_name='AChiliMountain')


def start_main(file_manager,path):
    file_manager.open_file(path)



file_manager = Directory_Manager(["/home/matias/Documents/mcutils/data/good bye.txt","/home/matias/Documents/mcutils/code"])
file_manager.filter_format(['txt','py'])
file_manager.print_info()


mmf_credits = Menu_Func(title="Credits",function=credits.print_credits)
mmf_exit = Menu_Func("Exit App",exit_application, *["Exiting Application"])
mmf_main = Menu_Func("Start main.py",start_main,*[file_manager,"/home/matias/Documents/mcutils/code/main.py"])


login_menu = Menu(title="Login",input_each=True,options=["User Name","Password"])
main_menu = Menu(title="Main Menu",options=[login_menu, mmf_credits, mmf_main, mmf_exit],back=False)




for dir in file_manager.get_dirs():
    print dir


while True:
    main_menu.show()