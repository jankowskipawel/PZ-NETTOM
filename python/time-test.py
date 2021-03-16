#!/var/www/html/cgi-enabled/env/bin/python3
import pymysql
import datetime
print("Content-type: text/html\n\n")
print("<html>\n<body>")
print( "<div style=\"width: 100%; font-size: 24px; text-align: center;\">")

db = pymysql.connect(host='192.168.0.27',
                             user='root',
                             password='PzNettom2021!',
                             database='CSV_DB' )
cursor = db.cursor()
datestart = datetime.datetime.now()
sql = "SELECT * FROM covid ORDER BY location ASC"
cursor.execute(sql)
#result = cursor.fetchone()
#print(result)
db.close()
dateend = datetime.datetime.now()
print(f"start: {datestart}, end: {dateend}")

print("</div>\n</body>\n</html>")
