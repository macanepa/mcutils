def exit_application(text = None):
    if(text != None):
        print text
    exit(0)


def register_error(error_string, print_error = True):
    if(print_error == True):
        print "Error Encountered <%s>" % error_string

def clear(n=1):
    print "\n"*n

class Credits:
    def __init__(self,authors = [], company_name = "",team_name = "", github_account="", email_address=""):
        self.authors = authors
        self.company_name = company_name
        self.team_name = team_name
        self.github_account = github_account
        self.email_address = email_address


    def print_credits(self):
        print ">> Credits <<"
        if(self.company_name != ""):
            print "Company: %s"%self.company_name
        if(self.team_name != ""):
            print "Developed by %s"%self.team_name
        if(len(self.authors)!=0):
            print "\nAuthors:"
            for author in self.authors:
                print "\t-%s"%author
        print
        if(self.email_address != ""):
            print "Email: %s"%self.email_address
        if(self.github_account != ""):
            print "GitHub: %s"%self.github_account
        raw_input("\nPress Enter to Continue...")


class Menu_Func:
    def __init__(self,function,title=None,*args):
        self.function = function
        self.title = title
        self.args = args

    def print_function_info(self):
        print "Function: %s" % self.function

        for parameter in self.args:
            print parameter

    def get_unassigned_params(self):
        unassigned_parameters_list = []
        for parameter in self.function.func_code.co_varnames:
            if not parameter in (self.args):
                print parameter
                unassigned_parameters_list.append(parameter)
        return unassigned_parameters_list

    def get_args(self):
        print self.args
        return self.args

    def call_function(self):
        self.function(*self.args)



class Menu:

    def __init__(self,title = None, subtitle = None,text = None,options=[],return_type=int,parent=None,input_each = False,previous_menu=None,back=True):
        self.title = title
        self.subtitle = subtitle
        self.text = text
        self.options = options
        self.return_type = return_type
        self.parent = parent
        self.input_each = input_each
        self.previous_menu = previous_menu
        self.back = back

    def set_parent(self,parent):
        self.parent = parent

    def set_previous_menu(self,previous_menu):
        self.previous_menu = previous_menu

    def get_input(self,format=">> ",can_exit=True,exit_input="exit"):
        user_input = raw_input(format)

        if(user_input == exit_input):
            if (can_exit):
                exit_application()
            else:
                register_error("Can exit application now")

        return user_input

    def get_selection(self, exit_input="exit"):

        start_index = 1
        if(self.back):
            start_index=0


        # if there exist options it means user have to select one of them
        if((self.options.__len__()!=0) and (not self.input_each)):

            while True:

                selection = self.get_input()

                if(selection.__str__().isdigit()):
                    if(int(selection) in range(start_index,(self.options.__len__())+1)):
                        if(int(selection) != 0):
                            if (isinstance(self.options[int(selection) - 1], Menu_Func)):
                                function = self.options[int(selection) - 1]
                                function.call_function()
                            elif (isinstance(self.options[int(selection) - 1], Menu)):
                                sub_menu = self.options[int(selection) - 1]
                                sub_menu.set_parent(self)
                                sub_menu.print_menu()
                        else:
                            if(self.parent != None):
                                self.parent.set_previous_menu(self)
                                self.parent.print_menu()
                        break
                    else:
                        register_error("Index not in range")

                else:
                    register_error("Entered must be int.")

        elif(self.input_each):
            selection = []
            for option in self.options:
                parameter_value = self.get_input(str(option)+" >> ")
                selection.append(parameter_value)

        # if there aren't any option it means user must input a string
        else:
            selection = self.get_input()

        return selection


    def print_menu(self):
        # if(self.previous_menu != None) and (self != self.previous_menu):
        #     del(self.previous_menu)
        clear()
        if(self.title != None):
            print self.title
        if (self.subtitle != None):
            print self.subtitle
        print
        if (self.text != None):
            print self.text

        # print "Parent:",self.parent


        if(self.options.__len__()!=0 and (not self.input_each)):
            for option_index in range(len(self.options)):
                if isinstance(self.options[option_index], Menu_Func):
                    print "%s. %s" % (str(option_index + 1), self.options[option_index].title)
                elif isinstance(self.options[option_index],Menu):
                    print "%s. %s"%(str(option_index+1),self.options[option_index].title)
                else:
                    print "%s. %s"%(str(option_index+1),self.options[option_index])
            if (self.back):
                print "0. Back"

        selected_option = self.get_selection()
        return selected_option
