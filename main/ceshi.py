import pymysql

db = pymysql.connnet("localhost","3306",user="root",password="123456",db="test")
pymysql.connect

cursor = db.cursor();

sql = "Select * from USER WHERE id = '%d'" % (1)

try:
    cursor.execute(sql)
    results = cursor.fetchall()
    for row in results :
        id = row[0]
        name = row[1]
        age = row[2]
        sex = row[3]
        remark = row[4]
        print("id=%s,name=%s,age=%s,sex=%s,remark=%s" % \
              (id,name,age,sex,remark))
except :
    print("ERROR: unable to fetch data")
db.close()


