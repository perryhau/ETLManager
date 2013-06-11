#! /usr/bin/env python

from optparse import OptionParser
from settingsParser import settings_parser
from connector import db_connection
from FileReader import FileReader
from datetime import datetime
from createTable import table_creator

class importFile():
    
    def __init__(self, file_name, tbl_name, tbl_type, settings_file = "../chris_home.xml", inc_header = False, start_line = 0, file_del = "auto"):
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
                
                
                
                # create table if needed
                if tbl_type == "new":
                    if inc_header == True:
                        tbl_cr = table_creator(content, tbl_name, header = header)
                    else:
                        tbl_cr = table_creator(content, tbl_name)
                    
                    new_tbl_stmt = tbl_cr.return_newTableStmt()
                    db_conn.run_query(new_tbl_stmt)
                    print "table %s created!" % tbl_name
                
                    header = tbl_cr.return_header()
                
                ## try inserting the lines
                for line in content:
                    
                    ### prepare the insert statement for the line
                    i = 0
                    ins_stmt = "insert into " + tbl_name + " ("
                    for t in range(len(line)):
                        ins_stmt += header[t]
                        if t+1 < len(line):
                            ins_stmt += ", "
                    ins_stmt += ") values ("
                    for el in line:
                        el = str(el)
                        ins_stmt += " '" + el.replace('\'', "\'") + "'"
                        if i+1 < len(line):
                            ins_stmt += ", "
                        i += 1
                    ins_stmt += ")"
                    
                    ### insert the line:
                    #print ins_stmt
                    try:
                        db_conn.run_query(ins_stmt)
                    except:
                        print "This didn't work:\n " + ins_stmt
                
                ## logging the import job
            
            #closing the db:
            if db_conn:
                db_conn.close()    
    
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