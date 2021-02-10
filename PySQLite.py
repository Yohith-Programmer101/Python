import sqlite3
import os

os.chdir("SQLite")

try:
    conn = sqlite3.connect("practise.db")
    cursor = conn.cursor()

    sql = '''SELECT * FROM people;'''

    cursor.execute(sql)
    conn.commit()
    print("Query ok")
    for i in cursor:
        print(i)
    cursor.close()

except sqlite3.Error as e:
    print("ERROR", e)
finally:

    if conn == True:
        conn.close()
        print("Connection closed.")