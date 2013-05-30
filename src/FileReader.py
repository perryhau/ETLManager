#! /usr/bin/env python
#FileReader module and class. 

import csv

class FileReader:
    file1 = 'filename'
    
    
    def __init__(self, filename):
        self.file1 = filename
        #print filename
        
    def get_line(self, line, delimit):
        fo = open(self.file1, 'r', 1)
        lines = fo.readlines()
        arr = lines[line].strip().split(delimit)
        return arr
    
    def discover_delimiter(self, starting_line = 0):
        foundDel = ''
        max_dels = {'comma':0, 'tab':0, 'pipe':0, 'semi':0}
        num_lines = 0
        
        with open(self.file1) as infp:
            t = 0
            for line in infp:
                if t >= starting_line:
                    num_lines += 1
                t += 1
                
        if num_lines > 500:
            num_lines = 500
        
        fo = open(self.file1, 'r', 1)
        lines = fo.readlines()
        
        for i in range(num_lines):
            arr = lines[i+starting_line].split(',')
            if max_dels['comma'] < len(arr):
                max_dels['comma'] = len(arr)
        
        for i in range(num_lines):
            arr = lines[i+starting_line].split('\t')
            if max_dels['tab'] < len(arr):
                max_dels['tab'] = len(arr)
                
        for i in range(num_lines):
            arr = lines[i+starting_line].split('|')
            if max_dels['pipe'] < len(arr):
                max_dels['pipe'] = len(arr)
        
        for i in range(num_lines):
            arr = lines[i+starting_line].split(';')
            if max_dels['semi'] < len(arr):
                max_dels['semi'] = len(arr)
        
        foundDel = max(max_dels, key=max_dels.get)
        print "The delimiter found is: " + foundDel
        return foundDel

    def readTextFile (self):
        fo = open(self.file1, 'r', 1)
        l = []
        for line in fo.readlines():
            line = line.strip()
            if len(line) > 0:
                l.append(line)
        fo.close()
        return l
    
    def readTextToArray (self, delimit, starting_line = 0, quote_char = None):
        fo = open(self.file1, 'r', 1)
        arr = []
        i = 0
        
        for line in fo.readlines():
            if i >= starting_line:
                line = line.strip()
                if len(line) > 0:
                    arr.append(line.split(delimit))
            i += 1
            
        fo.close()
        return arr
    
    def readTextToDictionary (self, delimit):
        fo = open(self.file1, 'r', 1)
        dic = {}
        for line in fo.readlines():
            line = line.strip()
            arr = line.split(delimit)
            if len(line) > 0:
                dic[arr[0]] = arr[1]
        
        fo.close()
        return dic

    def useDifferentFile(self, filename):
        self.file1 = filename
