import pymysql

# 打开数据库连接
db = pymysql.connect("localhost", "root", "123456", "wwz")

# 使用cursor()方法获取操作游标
cursor = db.cursor()

# SQL 插入语句
sql = """INSERT INTO student(Sno,Sname, Age, Sex) VALUES (1000, 'Tom', 25, 'f')"""
try:
    cursor.execute(sql)
    db.commit()
    print("执行try")
except:
    db.rollback()
    print("执行except")

db.close()
