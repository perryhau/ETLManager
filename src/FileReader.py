#! /usr/bin/env python
#FileReader module and class. 

import csv

class FileReader:
    file1 = 'filename'
    
    
    def __init__(self, filename):
        self.file1 = filename
        #print filename
        
<<<<<<< HEAD
    def get_line(self, line, delimit):
        fo = open(self.file1, 'r', 1)
        lines = fo.readlines()
        arr = lines[line].strip().split(delimit)
        return arr
    
    def discover_delimiter(self, starting_line = 0):
=======
    def discover_delimiter(self, start_line = 0):
>>>>>>> branch 'refs/heads/master' of https://github.com/d3ngar/ETLManager.git
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
<<<<<<< HEAD
            arr = lines[i+starting_line].split(',')
            if max_dels['comma'] < len(arr):
                max_dels['comma'] = len(arr)
=======
            if i + start_line < num_lines:
                arr = lines[i + start_line].split(',')
                if max_dels['comma'] < len(arr):
                    max_dels['comma'] = len(arr)
>>>>>>> branch 'refs/heads/master' of https://github.com/d3ngar/ETLManager.git
        
        for i in range(num_lines):
<<<<<<< HEAD
            arr = lines[i+starting_line].split('\t')
            if max_dels['tab'] < len(arr):
                max_dels['tab'] = len(arr)
=======
            if i + start_line < num_lines:
                arr = lines[i + start_line].split('\t')
                if max_dels['tab'] < len(arr):
                    max_dels['tab'] = len(arr)
>>>>>>> branch 'refs/heads/master' of https://github.com/d3ngar/ETLManager.git
                
        for i in range(num_lines):
<<<<<<< HEAD
            arr = lines[i+starting_line].split('|')
            if max_dels['pipe'] < len(arr):
                max_dels['pipe'] = len(arr)
=======
            if i + start_line < num_lines:
                arr = lines[i + start_line].split('|')
                if max_dels['pipe'] < len(arr):
                    max_dels['pipe'] = len(arr)
>>>>>>> branch 'refs/heads/master' of https://github.com/d3ngar/ETLManager.git
        
        for i in range(num_lines):
<<<<<<< HEAD
            arr = lines[i+starting_line].split(';')
            if max_dels['semi'] < len(arr):
                max_dels['semi'] = len(arr)
=======
            if i + start_line < num_lines:
                arr = lines[i + start_line].split(';')
                if max_dels['semi'] < len(arr):
                    max_dels['semi'] = len(arr)
>>>>>>> branch 'refs/heads/master' of https://github.com/d3ngar/ETLManager.git
        
        foundDel = max(max_dels, key=max_dels.get)
<<<<<<< HEAD
        print "The delimiter found is: " + foundDel
=======
        fo.close()
        
        print "found delimiter: " + foundDel
>>>>>>> branch 'refs/heads/master' of https://github.com/d3ngar/ETLManager.git
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
    
<<<<<<< HEAD
    def readTextToArray (self, delimit, starting_line = 0, quote_char = None):
=======
    def readTextToArrayList (self, delimit, start_line = 0):
        
        trans = { 'semi':';', 'pipe':'|', 'tab':'\t', 'comma':','}
        
>>>>>>> branch 'refs/heads/master' of https://github.com/d3ngar/ETLManager.git
        fo = open(self.file1, 'r', 1)
        arr = []
        i = 0
        
<<<<<<< HEAD
        for line in fo.readlines():
            if i >= starting_line:
                line = line.strip()
                if len(line) > 0:
                    arr.append(line.split(delimit))
            i += 1
            
=======
        lines = fo.readlines()
        
        for l in range(len(lines)):
            if l + start_line < len(lines):
                line = lines[l + start_line].strip()
                arr0 = line.split(trans[delimit])
                arr1 = []
                for el in arr0:
                    arr1.append(el.strip())
                arr.append(arr1)
>>>>>>> branch 'refs/heads/master' of https://github.com/d3ngar/ETLManager.git
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
