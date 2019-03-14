# mcutils
Utilities Library

Developed by Matías Cánepa González

GitHub: http://github.com/macanepa

# Documentation
mcutils purpose is to ease the development cycle when creating console based programs with python.

## Current features

- Create easy and simple Menu cycles.
  - Title, Subtitle, Text
  - Options (list the different alternatives to choose from)
    - Submenus (Menu instance)
    - Functions (Menu_Func instance [must pass the arguments as *args])
  - Each menu is an instance from the Menu Class
    - Allows to return to previous menus (parent menu)
  - Controlled user input
- Error Handler
- Directory Manager
  - List files in directory
  - Filter through different file extensions
  - Open files with default application (cross-platform support)


## Future features
  - python 3.x support
  - Logger system

##### Supported versions 
- python 2.7+
