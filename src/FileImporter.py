#! /usr/bin/env python

from optparse import OptionParser
from settingsParser import settings_parser
from connector import db_connection
from FileReader import FileReader
from datetime import datetime

class importFile():
    
    def __init__(self):
        s = settings_parser()
        settings = s.initialize("../chris_home.xml")
        
        if settings['type'] == 'MySQL':
            db_conn = db_connection(self, settings['connection'], settings['user'], settings['password'], settings['db_name'])
        else:
            print "not recognised connection type"
            
        fr = FileReader("../testImportFile.txt")
        fr.discover_delimiter()
    
if __name__ == "__main__":
    
    col_head = False
    delimiter = 'auto'
    tbl_type = 'new'
    start_line = 0
    
    date_time = datetime.now()
    dtm = datetime.strftime(date_time, "%Y%m%d_%H%M%S")
    tbl_name = "temp_" + dtm
    
    
    parser = OptionParser()
    parser.add_option("-c", "--column_headers", dest="ch", help="Set True or False for column headers. Default is False", default=col_head)
    parser.add_option("-s", "--starting_line", dest="sl", help="What line of the file to start reading it. Default is 0.", default=col_head)
    parser.add_option("-d", "--delimiter", dest="d", help="File delimiter option (comma, pipe, semicolon, tab, excel, xml). Default is auto discover", default=delimiter)
    parser.add_option("-tt", "--table_option", dest="tt", help="Is the destination a new or existing table. Default is new.", default=tbl_type)
    parser.add_option("-tn", "--table_name", dest="tn", help="Destination table name. Default is temp_YYYYMMDD_HHMMSS.", default=tbl_name)
    
    (args, values) = parser.parse_args()
    
    start_date = args.start_date
    
    app = importFile()