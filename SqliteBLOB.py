import sqlite3

def convertToBinaryData(filename):
    file = open(filename, "rb")
    data = file.read()
    return data

def insertBLOB(ID, Name, Image):
    try:
        conn = sqlite3.connect("SQLite/SQLiteBLOB.db")
        cursor = conn.cursor()
        print("Connection successfull!")
        query = '''INSERT INTO sqliteblob
                VALUES (?, ?, ?);'''
        image = convertToBinaryData(Image)
        data_tuple = (ID, Name, image)
        cursor.execute(query, data_tuple)
        conn.commit()
        print("Image and file inserted successfully as a BLOB into a table")
        cursor.close()
    except sqlite3.Error as error:
        print("Failed to insert blob data into sqlite table", error)
    finally:
        if (conn):
            conn.close()
            print("Sqlite connection is closed.")

def writeTofile(data, filename):
    with open(filename, 'wb') as file:
        file.write(data)
    print("Stored blob data into: ", filename, "\n")

def readBlobData(empId):
    try:
        sqliteConnection = sqlite3.connect('SQLite/SQLiteBLOB.db')
        cursor = sqliteConnection.cursor()
        print("Connected to SQLite")

        sql_fetch_blob_query = """SELECT * from sqliteblob where id = ?"""
        cursor.execute(sql_fetch_blob_query, (empId,))
        record = cursor.fetchall()
        for row in record:
            print("Id = ", row[0], "Name = ", row[1])
            name  = row[1]
            photo = row[2]
            print("Storing employee image and resume on disk \n")
            photoPath = "./backups/" + name + ".jpg"
            writeTofile(photo, photoPath)
        cursor.close()

    except sqlite3.Error as error:
        print("Failed to read blob data from sqlite table", error)
    finally:
        if (sqliteConnection):
            sqliteConnection.close()
            print("sqlite connection is closed")

readBlobData(1)
readBlobData(2)