import pymysql

mydb = pymysql.connect(
    host = "localhost",
    user = "root",
    password = "password",
    database= "wsaa"
)

mycursor = mydb.cursor()
sql = "CREATE TABLE student (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), age INT)"

mycursor.execute(sql)

mycursor.close()
connection.close()