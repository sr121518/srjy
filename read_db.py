import pymysql

db = pymysql.connect(host='localhost',
                     port=3306,
                     user='root',
                     password='123456',
                     database='stu',
                     charset='utf8')

cur = db.cursor()

# name1 = input("请输入学生姓名:")
sql = "select name " \
      "from class " \
      "where score>%s and age>%s"
# print(sql)
cur.execute(sql,[70,8])
print(cur.fetchall())

# many_row = cur.fetchmany(2)
# print(many_row)



cur.close()
db.close()