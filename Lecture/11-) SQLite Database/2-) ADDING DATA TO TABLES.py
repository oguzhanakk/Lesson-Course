import sqlite3

con = sqlite3.connect("library.db")
cursor = con.cursor()

def table_creation():
    cursor.execute("CREATE TABLE IF NOT EXISTS Books(Name TEXT, Author TEXT, Publisher TEXT, Number_of_Pages INT)")
    con.commit()

def adding_data():
    cursor.execute("Insert into Books Values('istanbul hatirası','Ahmet umit', 'Everest', 561)")
    con.commit()

def adding_data2(name,author,publisher,number_of_pages):
    cursor.execute("Insert into Books Values(?,?,?,?)",(name,author,publisher,number_of_pages))
    con.commit()

Name = input("Name: ")
Author = input("Author: ")
Publisher = input("Publisher: ")
Number_of_Pages = input("Number_of_Pages: ")
adding_data2(Name,Author,Publisher,Number_of_Pages)

con.close()