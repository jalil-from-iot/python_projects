import sqlite3

# Connect to SQLLITE
connection = sqlite3.connect("player.db")

#  Create a cursor object to insert object,create table and retrive

cursor = connection.cursor()

table_info = """
Create table PLAYER(NAME VARCHAR(50), AGE INT,
GOALS INT);
"""

cursor.execute(table_info)

#  INSERT SOME MORE RECORDS

cursor.execute('''Insert Into PLAYER values('CRISTIANO RONALDO',39,885)''')

cursor.execute('''Insert Into PLAYER values('LEO MESSI',35,756)''')

cursor.execute('''Insert Into PLAYER values('Neymar Junior',32,347)''')

#  Display all the records 
print("the Inserted records are")
data = cursor.execute('''Select * From PLAYER''')

for row in data:
    print(row)

# Close the connection

connection.commit()
connection.close()