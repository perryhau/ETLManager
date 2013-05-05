#! /usr/bin/env python

import Tkinter as tk
import menu_bar
import importWindow as iw

class ETLManager():
    
    def append_to_log(self, text):
        self.text_area.config(state = "normal")
        self.text_area.insert("end", text + '\n')
        self.text_area.config(state = "disabled")
    
    def b_import(self):
        imp = iw.import_window(self)
        self.append_to_log("import selected")
    
    def initialize(self):
        self.main_win = tk.Tk()
        self.main_win.title("ETL Manager")
        self.main_win.geometry("500x370+200+200")
        
        ## Menu Bar
        mb = tk.Menu(self.main_win)
        menu_bar.ret_menu_bar(mb)
        self.main_win.config(menu = mb)
        
        ## Other stuff
        self.import_button = tk.Button(self.main_win, text="Import...", command = self.b_import, height = 5, width=15)
        self.im_schedule_button = tk.Button(self.main_win, text="Import Schedule...", command = self.b_import, height = 5, width=15)
        self.report_button = tk.Button(self.main_win, text="Reporting...", command = self.b_import, height = 5, width=15)
        
        self.online_button = tk.Button(self.main_win, text="Internet...", command = self.b_import, height = 5, width=15)
        self.extract_button = tk.Button(self.main_win, text="Extract...", command = self.b_import, height = 5, width=15)
        self.ex_schedule_button = tk.Button(self.main_win, text="Export Schedule...", command = self.b_import, height = 5, width=15)
        
        self.text_area = tk.Text(self.main_win, height = 12, width = 63, bg="black", fg="green")
        
        self.import_button.grid(row = 0, column = 0, sticky="nw")
        self.im_schedule_button.grid(row = 0, column = 1, sticky="nw")
        self.report_button.grid(row = 0, column = 2, sticky="nw")
        self.online_button.grid(row = 1, column = 0, sticky="nw")
        self.extract_button.grid(row = 1, column = 1, sticky="nw")
        self.ex_schedule_button.grid(row = 1, column = 2, sticky="nw")
        self.text_area.grid(row = 2, column = 0, columnspan = 3, sticky="nw")
        
    
    def __init__(self, parent):
        self.parent = parent
        self.initialize()
        
        

if __name__ == "__main__":
    app = ETLManager(None)
    app.main_win.mainloop()