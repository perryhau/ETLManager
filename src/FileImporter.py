#! /usr/bin/env python

from optparse import OptionParser
from settingsParser import settings_parser
from connector import db_connection
from FileReader import FileReader
from datetime import datetime

class importFile():
    
    def __init__(self, file_name, tbl_name, tbl_type, settings_file = "../chris_home.xml", inc_header = False, start_line = 8, file_del = "auto"):
        if (file_name == None or tbl_name == None):
            print "Must declare at least file to import. Start with -f FILE_NAME. Better luck next time!"
        else:
            s = settings_parser()
            settings = s.initialize(settings_file)
        
            if settings['type'] == 'MySQL':
                db_conn = db_connection(self, settings['connection'], settings['user'], settings['password'], settings['db_name'])
            else:
                print "not recognised connection type"
        
            if file_del <> "excel" and file_del <> "xml":
                fr = FileReader(file_name)
                
                if file_del == "auto":
                    file_del = fr.discover_delimiter(starting_line = start_line)
            
                if inc_header == True :
                    header_line = start_line
                    header = fr.get_line(header_line, file_del)
                
                if inc_header == True : 
                    content = fr.readTextToArrayList(file_del, st_line = start_line+1)
                else:
                    content = fr.readTextToArrayList(file_del, st_line = start_line)
                
                
                # Only when headers:
                if inc_header == True : 
                    ## determine if all columns have a header
                    max_cols = len(header)
                    for i in content:
                        ileng = len(i)
                        if ileng > max_cols:
                            max_cols = ileng
                            
                    ## add col_headers if not enough
                    if max_cols > len(header):
                        difference = max_cols - len(header)
                        for i in range(difference):
                            header.append("column_header_" + str(i))
                
                # create table if needed
                if tbl_type == "new":
                    if inc_header == False :
                        header = []
                        max_cols = 0
                        for i in content:
                            ileng = len(i)
                            if ileng > max_cols:
                                max_cols = ileng
                        for i in range(max_cols):
                            header.append("column_header_" + str(i))
                    
                    #print header

                    ### understand columns (Best int, then float last string)
                    col_datatype = {}
                    for t in range(len(header)):
                        col_datatype[t] = "int"
                    #print col_datatype
                    
                    for i in content:
                        n = 0
                        for t in i:
                            max_str_len = "strm_" + str(n)
                            
                            try:
                                a = col_datatype[max_str_len]
                            except KeyError, e:
                                col_datatype[max_str_len] = 0
                            
                            try:
                                t = int(t)
                            except ValueError:
                                #do nothing
                                print "No int",
                            if type(t) != type(int()):
                                try:
                                    t = float(t)
                                except ValueError:
                                    #do nothing
                                    print "No float",
                            
                            print type(t)
                            
                            if (type(t)==type(bool()) and (col_datatype[max_str_len] < 10 or col_datatype[max_str_len] == None)):
                                col_datatype[n] = "varchar"
                                col_datatype[max_str_len] = 10
                                
                            if ((type(t)==type(int())) or (type(t)==type(long()))) and col_datatype[n] != 'varchar' and col_datatype[n] != "float":
                                if (t >= 2000000000) or (t <= -2000000000):
                                    col_datatype[n] = "float"
                                else:
                                    col_datatype[n] = "int"
                            
                            if type(t)==type(float()) and col_datatype[n] != 'varchar':
                                col_datatype[n] = "float"
                            
                            if type(t)==type(str()):
                                col_datatype[n] = "varchar"
                                if (col_datatype[max_str_len] < len(t)) or col_datatype[max_str_len] == None:
                                    col_datatype[max_str_len] = len(t) + 100
                            
                            n += 1
                    
                    ### Try building a create table statement:
                    
                    stmt_cr = "create table " + tbl_name + " ("
                    i = 0
                    for col in header:
                        max_str_len = "strm_" + str(i)
                        stmt_cr += " " + col + " " + col_datatype[i]
                        if col_datatype[i] == "varchar":
                            stmt_cr += "(" + str(col_datatype[max_str_len]) + ")" 
                        if i+1 < len(header):
                            stmt_cr += "," 
                        i += 1
                    stmt_cr += ");"
                    
                    print stmt_cr
                    
                ## try inserting the lines
                
                ## logging the import job
                
    
if __name__ == "__main__":
    
    col_head = False
    delimiter = 'auto'
    tbl_type = 'new'
    start_line = 0
    quote_char = ""
    settings_file = "../default.xml"
    file_name = "../testImportFile.txt"
    
    date_time = datetime.now()
    dtm = datetime.strftime(date_time, "%Y%m%d_%H%M%S")
    tbl_name = "temp_" + dtm
    
    
    parser = OptionParser()
    parser.add_option("-f", "--import_file", dest="f", help="What file should be used for this import. This setting is MANDATORY. Use -f FILE_NAME to use", default=file_name)
    parser.add_option("-S", "--settings_file", dest="set", help="Loading a different database connection file. Default is ../chris_home.xml", default=settings_file)
    parser.add_option("-c", "--column_headers", dest="ch", help="Set True or False for column headers. Default is False", default=col_head)
    parser.add_option("-s", "--starting_line", dest="sl", help="What line of the file to start reading it. Default is 0.", default=col_head)
    parser.add_option("-d", "--delimiter", dest="d", help="File delimiter option (comma, pipe, semicolon, tab, excel, xml). Default is auto discover from plain text.", default=delimiter)
    parser.add_option("-t", "--table_option", dest="tt", help="Is the destination a new or existing table. Default is new.", default=tbl_type)
    parser.add_option("-n", "--table_name", dest="tn", help="Destination table name. Default is temp_YYYYMMDD_HHMMSS.", default=tbl_name)
    parser.add_option("-q", "--quote_char", dest="qc", help="The Quote Character. Usually is \" if the file uses one. The default value is not to utilise a quote char", default=quote_char)
    
    (args, values) = parser.parse_args()
    
    col_head = args.ch
    delimiter = args.d
    tbl_type = args.tt
    start_line = args.sl
    tbl_name = args.tn
    quote_char = args.qc
    file_name = args.f
    settings_file = args.set
    
    app = importFile(file_name, tbl_name, tbl_type)