#! /usr/bin/env python
#FileReader module and class. 

class FileReader:
    file1 = 'filename'
    
    
    def __init__(self, filename):
        self.file1 = filename

    def readTextFile (self):
        fo = open(self.file1, 'r', 1)
        l = []
        for line in fo.readlines():
            line = line.rstrip()
            if len(line) > 0:
                l.append(line)
        fo.close()
        return l
    
    def readTextToArray (self, delimit):
        fo = open(self.file1, 'r', 1)
        arr = []
        
        for line in fo.readlines():
            line = line.rstrip()
            if len(line) > 0:
                arr.append(line.split(delimit))
            
        fo.close()
        return arr
    
    def readTextToDictionary (self, delimit):
        fo = open(self.file1, 'r', 1)
        dic = {}
        for line in fo.readlines():
            line = line.rstrip()
            arr = line.split(delimit)
            if len(line) > 0:
                dic[arr[0]] = arr[1]
        
        fo.close()
        return dic

    def useDifferentFile(self, filename):
        self.file1 = filename
