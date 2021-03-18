#!/var/www/html/cgi-enabled/env/bin/python3
from config import *
import pymysql
import datetime
ram = "1GB"
print("Content-type: text/html\n\n")
print("<html>\n<body>")
print( "<div style=\"width: 100%; font-size: 12pt;\">")

cursor = db.cursor()
print( "<div style=\"width: 100%; font-size: 12pt;\">")
print( "<div style=\"width: 100%; font-weight: bold; font-size: 16pt;\">")
print(f"PYTHON (RAM: {ram})<br><br>")
print( "</div>")

print("Loading database...<br>")
totalTime = datetime.datetime.min
datestart = datetime.datetime.now()
sql = "SELECT * FROM covid ORDER BY location ASC"
cursor.execute(sql)
database = cursor.fetchall()
db.close()
dateend = datetime.datetime.now()
elapsedTime=dateend-datestart
totalTime+=elapsedTime
print(f"Loaded {len(database)} rows ({len(database[0])} columns each).<br>")
#database is List[List[str]]
print(f"Elapsed time (database load): {elapsedTime}   (Started: {datestart}, Finished: {dateend})<br><br>")
print("Executing script...<br>")

datestart = datetime.datetime.now()

############insert script here############
#print(database[0])

dateend = datetime.datetime.now()
elapsedTime=dateend-datestart
totalTime+=elapsedTime
print(f"Elapsed time (script execution): {elapsedTime}   (Started: {datestart}, Finished: {dateend})<br><br>")
print(f"Total time elapsed: {totalTime.strftime('%H:%M:%S.%f')}")
print("</div>\n</body>\n</html>")
