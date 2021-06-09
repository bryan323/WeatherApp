import sqlite3

conn = sqlite3.connect('TestDB.db') 
c = conn.cursor()

c.execute('''CREATE TABLE RAIN CHANCES
                ([generated_id] INTEGER PRIMARY KEY,[Chance_ID] integer, [Date_ID] text )''')

conn.commit()


print(conn.)
    
