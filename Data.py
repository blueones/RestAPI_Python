from psycopg2 import *


#def getweather(id):


class connectionStringFactory:
    def __init__(self,host,db,user,password):
        
        self.host=host
        self.db=db
        self.user=user
        self.password=password
        self.connectionString=self.createConnString()
        
    '''
    def test(self):
        print ("test")
    '''
    def createConnString(self):
        stringC="host="+self.host+" dbname="+self.db+" user="+self.user+" password="+self.password
        self.connString=stringC
        return stringC

    

        #cur.execute()

class dataintable:
    def __init__(self,connectionStringFactory):

        self.connectionString=connectionStringFactory.connectionString

    
    def tables(self):
        conn= connect(self.connectionString)
        cur=conn.cursor()
        cur.execute("""
        SELECT table_name FROM information_schema.tables WHERE table_schema='public' 
        """)

        for listtables in cur.fetchall():
            print (listtables)
        cur.close()
        conn.close()

    '''def get(self):
        self.cursor.execute("""
...     SELECT * FROM 
...     """

        )
    '''
    #def post(self,):




'''def getresult(connectionstring):

'''



'''class Weather:
    def __init__(self,id:int,point:Point,city:str,state:str,Address:str):

'''
