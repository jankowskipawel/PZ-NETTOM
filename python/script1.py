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
sql = "SELECT location, new_cases FROM covid"
cursor.execute(sql)
data = cursor.fetchall()
# database = []
# for row in rows:
#   database.append(row)
db.close()
dateend = datetime.datetime.now()
elapsedTime=dateend-datestart
totalTime+=elapsedTime
print(f"Loaded {len(data)} rows ({len(data[0])} columns each).<br>")
#data is List[List[str]]
print(f"Elapsed time (data load): {elapsedTime}   (Started: {datestart}, Finished: {dateend})<br><br>")
print("<br>Script output:<br><br>")

datestart = datetime.datetime.now()

############insert script here############
dict = {}
for i in data:
    location = i[0]
    if i[1] == '':
        new_cases = float(0)
    else:
        new_cases = float(i[1])
    if location in dict.keys():
        dict[location][0] += new_cases
        dict[location][1] += 1
    else:
        dict[location] = [new_cases, 1]

for i in dict:
    print(i + " " + str(dict[i][0] / dict[i][1]) + "<br>")


dateend = datetime.datetime.now()
elapsedTime=dateend-datestart
totalTime+=elapsedTime
print(f"<br>Elapsed time (script execution): {elapsedTime}   (Started: {datestart}, Finished: {dateend})<br><br>")
print(f"Total time elapsed: {totalTime.strftime('%H:%M:%S.%f')}")
print("</div>\n</body>\n</html>")
