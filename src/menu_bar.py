#! /usr/bin/env python

from Tkinter import *

def ret_menu_bar():
    menu_bar = Menu()
    
    ## File Menu
    file_menu = Menu(menu_bar, tearoff = 0)
    
    file_menu.add_command(label = "New...")
    file_menu.add_command(label = "Open...")
    file_menu.add_command(label = "Save")
    file_menu.add_command(label = "Save As...")
    file_menu.add_command(label = "Close...")
    
    menu_bar.add_cascade(label = "File", menu = file_menu)
    
    ## Settings Menu
    settings_menu = Menu(menu_bar, tearoff = 0)
    
    settings_menu.add_command(label = "Checkable")
    settings_menu.add_command(label = "Properties")
    
    menu_bar.add_cascade(label = "Settings", menu = settings_menu)
    
    ## Help Menu
    help_menu = Menu(menu_bar, tearoff = 0)
    
    help_menu.add_command(label = "Help")
    help_menu.add_command(label = "Online Help...")
    help_menu.add_command(label = "About")
    
    menu_bar.add_cascade(label = "Help", menu = help_menu)
    
    return