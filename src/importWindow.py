#! /usr/bin/env python

import Tkinter as tk
from datetime import datetime
import tkFileDialog
import re

class import_window():
    
    def button_okay(self):
        self.parent.append_to_log("Starting import with:")
        self.parent.append_to_log("\t -file name: " + self.file_n.get())
        self.parent.append_to_log("\t -contains header: " + str(self.header_cb.get()))
        self.parent.append_to_log("\t -read from line: " + str(self.import_line.get()))
        self.parent.append_to_log("\t -delimiter: " + self.del_var.get())
        self.parent.append_to_log("\t -new table: " + self.tbl_name.get())
        self.parent.append_to_log("\t -table name: " + self.tbl_type.get())
        
    def button_cancel(self):
        self.parent.append_to_log("Cancelled")
        self.import_window.destroy()
    
    def button_load(self):
        #self.parent.append_to_log("Load Button pressed")
        file_name = tkFileDialog.askopenfile()
        fn = re.search("'(.+?)'", str(file_name)).group(1)
        self.file_n.insert(0, fn)
    
    def initialize(self):
        self.import_window = tk.Toplevel()
        self.import_window.geometry("400x350+700+200")
        
        #Variables
        self.del_var = tk.StringVar()
        self.tbl_type = tk.StringVar()
        self.header_cb = tk.IntVar()
        
        ## load file line
        load_file_button = tk.Button(self.import_window, text = "load", command = self.button_load)
        load_file_button.grid(row=0, column=0, padx = 5, pady = 5)
        
        self.file_n = tk.Entry(self.import_window, width=35)
        self.file_n.grid(row=0, column=1, padx=0, pady=10, sticky="nw")
        
        ## main frame
        ### setting weight
        self.import_window.columnconfigure(1, weight=1)
        self.import_window.rowconfigure(1, weight=1)
        
        main_frame = tk.Frame(self.import_window)
        
        ### file options
        fo_frame = tk.Frame(main_frame)
        fo_frame.columnconfigure(1, weight=1)
        options_lbl = tk.Label(fo_frame, text="File Options:")
        options_lbl.grid(row=0, column=0, sticky="nw")
        
        si_lbl = tk.Label(fo_frame, text="start reading file at line: ")
        si_lbl.grid(row=1, column=0, padx=7, sticky="nw")
        self.import_line = tk.Entry(fo_frame, width=2)
        self.import_line.grid(row=1, column=1, sticky="nw")
        self.import_line.insert(0, "0")
        
        header_cb = tk.Checkbutton(fo_frame, text="first line contains column header", onvalue=1, offvalue=0, variable = self.header_cb)
        header_cb.grid(row=2, column=0, columnspan=2, padx=7)
        header_cb.select()
        
        fo_frame.grid(row=0, column=0, sticky="nw", pady=5)
        
        ## delimter options
        del_frame = tk.Frame(main_frame)
        delimiter_lbl = tk.Label(del_frame, text="Delimiter Options:")
        delimiter_lbl.grid(row=0, column=0, sticky="nw")
        
        rbg01_auto = tk.Radiobutton(del_frame, text="auto detect", variable = self.del_var, value="auto")
        rbg01_comma = tk.Radiobutton(del_frame, text="comma delimited", variable = self.del_var, value="comma")
        rbg01_semi = tk.Radiobutton(del_frame, text="semicolon delimited", variable = self.del_var, value="semi")
        rbg01_pipe = tk.Radiobutton(del_frame, text="pipe delimited", variable = self.del_var, value="pipe")
        rbg01_tab = tk.Radiobutton(del_frame, text="tab delimited", variable = self.del_var, value="tab")
        rbg01_xml = tk.Radiobutton(del_frame, text="xml delimited", state="disabled", variable = self.del_var, value="xml")
        rbg01_excel = tk.Radiobutton(del_frame, text="excel delimited", state="disabled", variable = self.del_var, value="excel")
        
        rbg01_auto.grid(row=1, column=0, sticky="nw", padx=7)
        rbg01_comma.grid(row=2, column=0, sticky="nw", padx=7)
        rbg01_tab.grid(row=3, column=0, sticky="nw", padx=7)
        rbg01_excel.grid(row=4, column=0, sticky="nw", padx=7)
        rbg01_semi.grid(row=2, column=1, sticky="nw", padx=7)
        rbg01_pipe.grid(row=3, column=1, sticky="nw", padx=7)
        rbg01_xml.grid(row=4, column=1, sticky="nw", padx=7)
        
        rbg01_auto.select()
        del_frame.grid(row=1, column=0, sticky="nw", pady=5)
        
        ### destination table options
        dest_frame = tk.Frame(main_frame)
        dest_lbl = tk.Label(dest_frame, text="Destination Options:")
        dest_lbl.grid(row=0, column=0, sticky="nw")
        
        rbg02_tablename_new = tk.Radiobutton(dest_frame, text="new table", variable=self.tbl_type, value = "new")
        rbg02_tablename_old = tk.Radiobutton(dest_frame, text="existing table", variable=self.tbl_type, value="existing")
        rbg02_tablename_new.select()
        tbl_name_lbl = tk.Label(dest_frame, text="table name")
        self.tbl_name = tk.Entry(dest_frame, width=20)
        date_time = datetime.now()
        dtm = datetime.strftime(date_time, "%Y%m%d_%H%M%S")
        self.tbl_name.insert(0, "temp_" + dtm)
        
        rbg02_tablename_new.grid(row=1, column=0)
        rbg02_tablename_old.grid(row=1, column=1)
        tbl_name_lbl.grid(row=2,column=0)
        self.tbl_name.grid(row=2, column=1)
        
        dest_frame.grid(row=2, column=0, sticky="nw", pady=5)
        
        main_frame.grid(row=1, column=0, columnspan=2, sticky="nw", pady=5)
        
        ## command line
        okay_button = tk.Button(self.import_window, text = "Go!", command = self.button_okay)
        cancel_button = tk.Button(self.import_window, text = "Cancel", command = self.button_cancel)
        
        okay_button.grid(row=2, column=1, sticky = "ne", padx=5, pady=5)
        cancel_button.grid(row=2, column=0, sticky = "nw", padx=5, pady=5)
    
    
    def __init__(self, parent):
        self.parent = parent
        self.initialize()
        
    
