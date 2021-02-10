import pymysql

db = pymysql.connect("localhost", "root", "", "pymysql")
cursor = db.cursor()
sql = "SELECT * FROM data"
try:
    cursor.execute(sql)
    db.commit()
except:
    db.rollback()
for i in cursor:
    id = i[0]
    name = i[1]
    lastname = i[2]
    print(f'''{id}     {name}      {lastname}''')
db.close()