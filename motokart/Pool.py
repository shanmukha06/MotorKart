import pymysql as mysql
def ConnectionPool():
    db=mysql.connect(host="localhost",port=3306,user="root",password="Rajesh@1521",db="motokart")
    cmd=db.cursor()
    return (db,cmd)
