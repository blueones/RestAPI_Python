import psycopg2
from psycopg2 import sql

#def getweather(id):
class Point:
    def __init__(self,latitude:float,longitude:float):
        self.latitude=latitude
        self.longitude=longitude

class Record:
    def __init__(self,city:str, state:str, point:Point,temperature:int):
        self.city=city
        self.state=state
        self.point=point
        self.temp=temperature

    def jsonToRecord(self,json):
        return Record(
            json['city'],
            json['state'],
            Point(json['point'][0],json['point'][1]),
            json['temperature'],
        )

class connectionStringFactory:
    def __init__(self,host,db,user,password):
        
        self.host=host
        self.db=db
        self.user=user
        self.password=password
        
        
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
    def __init__(self,host,db,user,password):

        self.connectionString=connectionStringFactory(host,db,user,password).createConnString()
        
    
    def tables(self):
        conn= psycopg2.connect(self.connectionString)
        cur=conn.cursor()
        cur.execute("""
        SELECT table_name FROM information_schema.tables WHERE table_schema='public' 
        """)
        listOfTables=cur.fetchall()
        cur.close()
        conn.close()
        
        return listOfTables

    def get(self):
        conn= psycopg2.connect(self.connectionString)
        cur=conn.cursor()
        tablename=self.tables()[0][0]
        print (tablename)
        cur.execute(sql.SQL("SELECT * FROM {}")
        .format(sql.Identifier(tablename))
        )
        
        tableContent=cur.fetchall()
        cur.close()
        conn.close()
        return tableContent

    
    #def post(self,):




'''def getresult(connectionstring):

'''



'''class Weather:
    def __init__(self,id:int,point:Point,city:str,state:str,Address:str):

'''
