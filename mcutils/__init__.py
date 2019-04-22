# -*- coding: utf-8 -*-

"""Top-level package for mcutils."""

__author__ = """Matias Canepa"""
__email__ = 'macanepa@miuandes.cl'
__version__ = '0.0.5'


# -*- coding: utf-8 -*-

"""Main module."""

from .logger import Log_Manager
from .input_validation import input_validation

Log = Log_Manager(developer_mode=True)

def exit_application(text=None):
    if (text != None):
        print(text)
    Log.log("Exiting Application Code:0")
    exit(0)

def register_error(error_string, print_error=False):
    message = "Error Encountered <{}>".format(error_string)
    if (print_error == True):
        print(message)
    Log.log(message)


# TODO: Implement parameters support for validation_function
def get_input(format=">> ", text=None, can_exit=True, exit_input="exit", valid_options=[], return_type=str, validation_function=None):

    if (text != None):
        print(text)
    while True:
        user_input = input(format)

        # Emergency exit system
        if (user_input == exit_input):
            if (can_exit):
                exit_application()
            else:
                register_error("Can't exit application now")

        # This is the build-in validations system
        if(validation_function != None):
            validation = validation_function.__call__(user_input)

        # This is the external validation system
        else:
            # from input_validation import input_validation
            validation = input_validation(user_input=user_input, return_type=return_type, valid_options=valid_options)
        if (validation):
            break

        register_error("Not Valid Entry")



    return user_input


def clear(n=3):
    print("\n" * n)


class Credits:
    def __init__(self, authors=[], company_name="", team_name="", github_account="", email_address=""):
        self.authors = authors
        self.company_name = company_name
        self.team_name = team_name
        self.github_account = github_account
        self.email_address = email_address

    def print_credits(self):
        clear(100)
        print(">> Credits <<")
        if (self.company_name != ""):
            print("Company: {}".format(self.company_name))
        if (self.team_name != ""):
            print("Developed by {}".format(self.team_name))
        if (len(self.authors) != 0):
            print("\nAuthors:")
            for author in self.authors:
                print("\t-{}".format(author))
        print
        if (self.email_address != ""):
            print("Email: {}".format(self.email_address))
        if (self.github_account != ""):
            print("GitHub: {}".format(self.github_account))
        input("\nPress Enter to Continue...")


class Menu_Function:
    def __init__(self, title=None, function=None, *args):
        self.function = function
        self.title = title
        self.args = args

    def print_function_info(self):
        print("Function: {}".format(self.function))

        for parameter in self.args:
            print(parameter)

    def get_unassigned_params(self):
        unassigned_parameters_list = []
        for parameter in self.function.func_code.co_varnames:
            if not parameter in (self.args):
                print(parameter)
                unassigned_parameters_list.append(parameter)
        return unassigned_parameters_list

    def get_args(self):
        print(self.args)
        return self.args

    def call_function(self):
        self.function(*self.args)


class Menu:

    def __init__(self, title=None, subtitle=None, text=None, options=[], return_type=int, parent=None, input_each=False,
                 previous_menu=None, back=True):
        self.title = title
        self.subtitle = subtitle
        self.text = text
        self.options = options
        self.return_type = return_type
        self.parent = parent
        self.input_each = input_each
        self.previous_menu = previous_menu
        self.back = back
        self.returned_value = None

    def set_parent(self, parent):
        self.parent = parent

    def set_previous_menu(self, previous_menu):
        self.previous_menu = previous_menu

    def get_selection(self, exit_input="exit"):

        start_index = 1
        if (self.back):
            start_index = 0

        # if there exist options it means user have to select one of them
        if ((self.options.__len__() > 0) and (not self.input_each)):

            while True:

                selection = get_input(return_type=int,)

                if (int(selection) in range(start_index, (self.options.__len__()) + 1)):
                    if (int(selection) != 0):
                        if (isinstance(self.options[int(selection) - 1], Menu_Function)):
                            function = self.options[int(selection) - 1]
                            function.call_function()
                        elif (isinstance(self.options[int(selection) - 1], Menu)):
                            sub_menu = self.options[int(selection) - 1]
                            sub_menu.set_parent(self)
                            sub_menu.show()
                    else:
                        if (self.parent != None):
                            self.parent.set_previous_menu(self)
                            self.parent.show()
                    break
                else:
                    register_error("Index not in range")

        elif (self.input_each):
            selection = {}
            if(isinstance(self.options,list)):
                for option in self.options:
                    parameter_value = get_input(str(option) + " >> ")
                    selection[option] = parameter_value
            elif(isinstance(self.options,dict)):
                for key in self.options:
                    parameter_value = get_input(format = key + " >> ",
                                                return_type=self.options[key][0],
                                                valid_options=self.options[key][1:])
                    selection[key] = parameter_value

        # if there aren't any option it means user must input a string
        else:
            selection = get_input()

        self.returned_value = selection
        return selection

    def show(self):
        # if(self.previous_menu != None) and (self != self.previous_menu):
        #     del(self.previous_menu)
        clear()
        if (self.title != None):
            print("/// {}".format(self.title))
        if (self.subtitle != None):
            print("///{}".format(self.subtitle))
        print
        if (self.text != None):
            print(self.text)

        if (self.options.__len__() > 0 and (not self.input_each)):
            for option_index in range(len(self.options)):
                if isinstance(self.options[option_index], Menu_Function):
                    print("{}. {}".format(str(option_index + 1), self.options[option_index].title))
                elif isinstance(self.options[option_index], Menu):
                    print("{}. {}".format(str(option_index + 1), self.options[option_index].title))
                else:
                    print("{}. {}".format(str(option_index + 1), self.options[option_index]))
            if (self.back):
                print("0. Back")

        selected_option = self.get_selection()
        return selected_option


class Directory_Manager:
    class File:
        def __init__(self, path, name, extension, size):
            self.path = path
            self.name = name
            self.extension = extension
            self.size = size

        def print_info(self):
            print("Name:", self.name)
            print("Path:", self.path)
            print("Extension:", self.extension)
            print("Size:", self.size)
            print

        # Modify delete function
        def delete_file(self):
            print("Deleting File <{}>".format(self.path))
            import os
            os.remove(self.path)

    def __init__(self, directories=[]):
        self.directories = directories
        self.files = []
        self.selected_files = []
        self.get_files()

    def get_dirs(self):
        dirs_list = []
        for file in self.files:
            dirs_list.append(file.path)
        return dirs_list

    # Retrieves a list of Files in self.files
    def get_files(self):
        import os
        def create_file(directory, file_name=None):

            file_dir = directory
            if (file_name != None):
                file_dir = os.path.join(directory,file_name)
            else:
                file_name = file_dir.rsplit('\\', 1)[-1]

            file = self.File(file_dir, file_name, file_name.rsplit('.', 1)[-1], os.path.getsize(file_dir))
            self.files.append(file)

        for directory in self.directories:
            if (os.path.isdir(directory)):
                if (os.path.exists(directory)):
                    for file_name in os.listdir(directory):
                        create_file(directory, file_name)
                else:
                    register_error("Path \"{}\" doesn't exists".format(directory))
            elif (os.path.isfile(directory)):
                create_file(directory=directory)
            else:
                register_error("Path \"{}\" not found".format(directory))

    def print_files_info(self):
        for file in self.files:
            file.print_info()

    def filter_format(self, extensions=[]):
        new_files = []
        for file in self.files:
            if (file.extension in extensions):
                new_files.append(file)
        self.files = new_files

    def create_directory(self, directory):
        import os
        os.makedirs(directory)

    def open_file(self, file):
        import platform, os, subprocess
        current_os = platform.system()

        if(isinstance(file,self.File)):
            path = file.path
        elif(isinstance(file,str)):
            path = file

        if (os.path.isfile(path)):

            Log.log("Open File <{}> // current os {}".format(file, current_os))

            if (current_os == 'Linux'):
                subprocess.call(('xdg-open', path))
            elif (current_os == 'Widows'):
                os.startfile(path)
            elif (current_os == "Darwin"):
                subprocess.call(('open', path))
            else:
                register_error("OS not supported")

        else:
            register_error("File \"{}\" not found".format(path))

    def add_file_to_selection(self,*args):
        Log.log("Adding Files <{}> to Selection".format(args))
        files = None
        for arg in args:
            if isinstance(arg,self.File):
                files = [arg]
            elif isinstance(arg,list):
                files = list(arg)
            elif isinstance(arg,str):
                files = list(filter(lambda x: arg in x.name, self.files))
            if(files != None):
                self.selected_files += files
        return self.selected_files
    def clear_file_selection(self):
        self.selected_files.clear()
