#! /usr/bin/env python

from Tkinter import *
import tkMessageBox
import tkFileDialog
import time
import sys

def menu_open():
    #do nothing
    file_name = tkFileDialog.askopenfile()
    print file_name 
    #time.sleep(10)
    return
    
def menu_about():
    tkMessageBox.showinfo(title="ETL Manager About", message="This is an early version of an ETL Manager")
    #tkMessageBox.showerror(title="ETL Manager About", message="This is an early version of an ETL Manager")
    #tkMessageBox.showwarning(title="ETL Manager About", message="This is an early version of an ETL Manager")
    return
    
def menu_quit():
    check_exit = tkMessageBox.askyesno(title = "Quit?", message = "Do you really want to close?")
    if check_exit > 0:
        print "Closing the programme"
        quit(0)
    return

def ret_menu_bar(menu_bar):
    
    ## File Menu
    file_menu = Menu(menu_bar, tearoff = 0)
    
    file_menu.add_command(label = "New...")
    file_menu.add_command(label = "Open...", command = menu_open)
    file_menu.add_command(label = "Save")
    file_menu.add_command(label = "Save As...")
    file_menu.add_separator()
    file_menu.add_command(label = "Close...", command = menu_quit)
    
    menu_bar.add_cascade(label = "File", menu = file_menu)
    
    ## Settings Menu
    settings_menu = Menu(menu_bar, tearoff = 0)
    
    settings_menu.add_checkbutton(label = "Checkable")
    settings_menu.add_command(label = "Properties")
    
    menu_bar.add_cascade(label = "Settings", menu = settings_menu)
    
    ## Help Menu
    help_menu = Menu(menu_bar, tearoff = 0)
    
    help_menu.add_command(label = "Help")
    help_menu.add_command(label = "Online Help...")
    help_menu.add_command(label = "About", command = menu_about)
    
    menu_bar.add_cascade(label = "Help", menu = help_menu)
    