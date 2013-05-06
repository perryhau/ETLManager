#! /usr/bin/env python
#FileWriter module and class. 

class FileWriter:
    file1 = 'filename'
    
    def __init__(self, filename):
        self.file1 = filename
        
    def appendALine(self, line):
        fo = open(self.file1, "a")
        line = str(line)
        fo.write(line)
        fo.close()
    
    def writeArrayToFile(self, arr):
        fo = open(self.file1, "w")
        for line in arr:
            line = str(line)
            fo.write(line + "\n")
        fo.close()
        
    def appendArrayToFile(self,arr):
        fo = open(self.file1, "a")
        for line in arr:
            line = str(line)
            fo.write(line + "\n")
        fo.close()
        
    def writeArrayListToFile(self, arrays, delimiter):
        fo = open(self.file1, "w")
        for arr in arrays:
            i = 0
            for item in arr:
                i = i+1
                item = str(item)
                if i < len(arr):
                    fo.write(item + delimiter)
                else:
                    fo.write(item)
            fo.write("\n")
        fo.close()
        
    def appendArrayListToFile(self, arrays, delimiter):
        fo = open(self.file1, "a")
        for arr in arrays:
            i = 0
            for item in arr:
                item = str(item)
                i = i+1
                if i < len(arr):
                    fo.write(item + delimiter)
                else:
                    fo.write(item)
            fo.write("\n")
        fo.close()
        