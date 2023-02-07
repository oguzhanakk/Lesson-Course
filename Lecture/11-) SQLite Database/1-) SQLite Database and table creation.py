import sqlite3

#connection to sqlite3
#If there is a library.db data base, it will be connected to it, otherwise it will be created.
con = sqlite3.connect("library.db")

#imlec = cursor
cursor = con.cursor()
def table_creation():
    cursor.execute("CREATE TABLE IF NOT EXISTS Books(Name TEXT, Author TEXT, Publisher TEXT, Number_of_Pages INT)")
    con.commit()

table_creation()

#Close the cursor
con.close()