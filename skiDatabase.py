import sqlite3
import _sqlite3


#connect to database
connection = sqlite3.connect('appDatabase.db')

#create cursor
cursor = connection.cursor()


#create table
cursor.execute("""CREATE TABLE mountains (
        tempearature text,
        snowLevel text ,
        hours text     
        )""")



connection.commit()

connection.close()