#!/var/www/html/cgi-enabled/env/bin/python3
from config import *
import pymysql
print("Content-type: text/html\n\n")
print("<html>\n<body>")
print( "<div style=\"width: 100%; font-size: 40px; font-weight: bold; text-align: center;\">")

cursor = db.cursor()
cursor.execute("SHOW TABLES")
result = cursor.fetchone()
print(result)
sql = "SELECT * FROM covid ORDER BY new_cases LIMIT 5"
cursor.execute(sql)
result = cursor.fetchone()
print(result)
db.close()


print("</div>\n</body>\n</html>")
