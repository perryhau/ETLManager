#! /usr/bin/env python

class table_creator() :
    
    head = []
    new_table = ""
    
    def return_header(self):
        return self.head
    
    def return_newTableStmt(self):
        return self.new_table
    
    def __init__(self, array, tbl_name, header = None):
        # Only when headers:
        if header != None : 
            ##check if all columns have a header
            max_cols = len(header)
            for i in array:
                ileng = len(i)
                if ileng > max_cols:
                    max_cols = ileng
                            
            ## add col_headers if not enough
            if max_cols > len(header):
                difference = max_cols - len(header)
                for i in range(difference):
                    header.append("column_header_" + str(i))
            self.head = header
        
        if header == None :
            header = []
            max_cols = 0
            for i in array:
                ileng = len(i)
                if ileng > max_cols:
                    max_cols = ileng
            for i in range(max_cols):
                header.append("column_header_" + str(i))
            self.head = header
        
        #print self.head
        
        ### understand columns (Best int, then float last string)
        col_datatype = {}
        for t in range(len(self.head)):
            col_datatype[t] = "int"
            
        for i in array:
            n = 0
            for t in i:
                #print t
                max_str_len = "strm_" + str(n)
                  
                try:
                    a = col_datatype[max_str_len]
                except KeyError, e:
                    col_datatype[max_str_len] = 0
                    
                try:
                    t = int(t)
                except ValueError:
                    #do nothing
                    pass
                    #print "No int",
                if type(t) != type(int()):
                    try:
                        t = float(t)
                    except ValueError:
                        #do nothing
                        pass
                        #print "No float",
                            
                #print type(t)
                                
                if type(t)==type(int()) and col_datatype[n] != 'varchar' and col_datatype[n] != "float":
                    if (t >= 2000000000) or (t <= -2000000000):
                        col_datatype[n] = "float"
                    else:
                        col_datatype[n] = "int"
                            
                if type(t)==type(float()) and col_datatype[n] != 'varchar':
                    col_datatype[n] = "float"
                            
                if type(t)==type(str()):
                    col_datatype[n] = "varchar"
                    if (col_datatype[max_str_len] < len(t)) or col_datatype[max_str_len] == None:
                        col_datatype[max_str_len] = len(t) + 50
                            
                n += 1
                    
        ### Try building a create table statement:
        #print col_datatype
             
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
                    
        #print stmt_cr
        self.new_table = stmt_cr
        
        
        