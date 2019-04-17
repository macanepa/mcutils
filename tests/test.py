import mcutils as mc
import os

main_menu = mc.Menu(title="Main Menu",options=[1,2,3],back=False)
dir_manager = mc.Directory_Manager([os.getcwd()])
dir_manager.print_files_info()

while True:
    main_menu.show()
