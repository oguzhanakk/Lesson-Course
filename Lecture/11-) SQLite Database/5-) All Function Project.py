import sqlite3

con = sqlite3.connect("library.db")
cursor = con.cursor()

def table_creation():
    cursor.execute("CREATE TABLE IF NOT EXISTS Books(Name TEXT, Author TEXT, Publisher TEXT, Number_of_Pages INT)")
    con.commit()


def adding_data():
    cursor.execute("Insert into Books Values('istanbul hatirası','Ahmet umit', 'Everest', 561)")
    con.commit()


def adding_data2(name, author, publisher, number_of_pages):
    cursor.execute("Insert into Books Values(?,?,?,?)", (name, author, publisher, number_of_pages))
    con.commit()


def pulling_data():
    cursor.execute("Select * From Books")
    list = cursor.fetchall()
    print("Library table information...")
    for i in list:
        print(i)

def pulling_data2():
    cursor.execute("Select Name,Author From Books")
    list = cursor.fetchall()
    print("Library table information...")
    for i in list:
        print(i)

def pulling_data3(publisher):
    cursor.execute("Select * From Books where publisher = ?", (publisher,))
    list = cursor.fetchall()
    print("Library table information...")
    for i in list:
        print(i)

def update_data(old_publisher,new_publisher):
    cursor.execute("Update Books set Publisher = ? where Publisher = ?", (new_publisher,old_publisher))
    con.commit()

def delete_data(Author):
    cursor.execute("Delete from Books where Author = ?", (Author,))
    con.commit()

con.close()