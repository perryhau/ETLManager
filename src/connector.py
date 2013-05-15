import MySQLdb as mdb  


class db_connection():
    
    def __init__(self, parent, db_host, db_user, db_passwd, db_schema):
        self.parent = parent
        self.con = mdb.connect(host=db_host, user=db_user, passwd=db_passwd, db=db_schema)
        print "DB Connected"
        
        self.cursor = self.con.cursor ()
        
        
    
    def close(self):
        self.cursor.close()
        self.con.close()