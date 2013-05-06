#! /usr/bin/env python
from datetime import datetime
from FileWriter import FileWriter

class Logger:
    logName = ""
    log = "***New Log***"

    if __name__ == "__main__":
        import sys
        a = sys.argv[0]

    def __init__(self, ln):
        self.logName = ln
        dt = datetime.now()
        dt = datetime.strftime(dt, '%Y-%m-%d %H:%M:%S')
        self.log = self.log + " - " + ln + " " + dt + "\n"

    def logThis (self, text):
        print text
        self.log = self.log + text + "\n"
    
    def returnLog(self):
        return self.log
    
    def printLog(self):
        print self.log
        
    def printLogToFile(self, filename):
        fw = FileWriter(filename)
        fw.appendALine(self.log)
        