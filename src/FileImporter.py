#! /usr/bin/env python

from optparse import OptionParser
from settingsParser import settings_parser
from connector import db_connection
from FileReader import FileReader

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
    app = importFile()