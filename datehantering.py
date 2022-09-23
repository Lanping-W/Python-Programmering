
import pandas
import sqlite3
from pathlib import Path
import os


class Datahantering:
    
    def __init__(self,path:str,database_name:str):
        #first check if database whith the name 'database_name' already exists and delete it, 
        #then create a blank database which name is database_name
        if  os.path.isfile(database_name):
            os.remove(database_name)
        Path(database_name).touch
        self.path=path
        self.database=database_name
        
    def read_csv(self):
        #read csv file
        self.data = pandas.read_csv(self.path) 
        #print(self.data)
        
    def create_database(self):
        #create database and cursor
        self.conn = sqlite3.connect(self.database)
        self.c=self.conn.cursor()
      
    def seed_database(self,table_name:str):
        #write data to the database
        self.data.to_sql(table_name,self.conn,if_exists='append', index = False)
        self.table_name=table_name
        #create dataframe
        self.df = pandas.read_sql("SELECT * FROM "+ table_name, self.conn)
        #print(self.df)
        
    def clear_database(self,list_to_del:list):
        #remove unwanted columns
        self.df_efter = self.df.drop(columns=list_to_del)
        #use 0 replace all Nan    
        self.df_efter=self.df_efter.fillna(0)   
        print(self.df_efter)
        #save to the database
        self.df_efter.to_sql(self.table_name, self.conn, if_exists='append', index = False)
        #print(self.c.execute("SELECT * FROM " + self.table_name).fetchall())
        
        #commit command
        self.conn.commit()
    
        #close connection   
        self.conn.close()