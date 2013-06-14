import MySQLdb as mdb
import sys

class db_connection():
    
    def __init__(self, parent, db_host, db_user, db_passwd, db_schema):
        self.parent = parent
        try:
            self.con = mdb.connect(host=db_host, user=db_user, passwd=db_passwd, db=db_schema)
            print "DB Connected"
            self.cursor = self.con.cursor ()
        except mdb.Error, e:
            print "There was an error connecting to the db"
            print "Error %d: %s" % (e.args[0], e.args[1])
            sys.exit(1)
        
    
    def close(self):
        self.cursor.close()
        self.con.close()
        print "Db connection closed"
        
    def run_query(self, query):
        #print query
        self.cursor.execute(query)
        self.con.commit()
