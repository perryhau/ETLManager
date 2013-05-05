#! /usr/bin/env python

import Tkinter as tk
import menu_bar

class ETLManager():
    
    def initialize(self):
        self.main_win = tk.Tk()
        self.main_win.title("ETL Manager")
        self.main_win.geometry("550x350+200+200")
        
        self.main_win.config(menu = menu_bar.ret_menu_bar())
    
    def __init__(self, parent):
        self.parent = parent
        self.initialize()
        
        

if __name__ == "__main__":
    app = ETLManager(None)
    app.main_win.mainloop()