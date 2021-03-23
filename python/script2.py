#!/var/www/html/cgi-enabled/env/bin/python3
from MySQLdb import _mysql
from config import *
import datetime
import math
import random

ram = "1GB"
print("Content-type: text/html\n\n")
print("<html>\n<body>")
print( "<div style=\"width: 100%; font-size: 12pt;\">")
print( "<div style=\"width: 100%; font-size: 12pt;\">")
print( "<div style=\"width: 100%; font-weight: bold; font-size: 16pt;\">")
print(f"PYTHON (RAM:{ram})<br><br>")
print( "</div>")
              
totalTime = datetime.datetime.min
datestart = datetime.datetime.now()
db_mysqldb.query("""SELECT * FROM covid""")
r = db_mysqldb.store_result()
result = r.fetch_row(maxrows=0)
data_bytes = list(map(list,result))
data=[]
for x in data_bytes:
  tmp = []
  for y in x:
    tmp.append(y.decode('utf-8'))
  data.append(tmp)
print("Loading database...<br>")
dateend = datetime.datetime.now()
elapsedTime=dateend-datestart
totalTime+=elapsedTime
print(f"Loaded {len(data)} rows ({len(data[0])} columns each).<br>")
#data is List[List[str]]
print(f"Elapsed time (data load): {elapsedTime}   (Started: {datestart}, Finished: {dateend})<br><br>")
print("<br>Script output:<br><br>")

datestart = datetime.datetime.now()
############insert script here############

## Funkcja zamienia puste wartosci/stringi numeryczne na liczbę PI
#
def EmptyToPi(dataset):
    dataset = list(dataset)
    for row in range(len(dataset)):
        dataset[row] = list(dataset[row])
        for col in range(4, len(dataset[row])): #lecimy od 5ego, ponieważ poprzednie to faktyczne napisy
            if (dataset[row][col] == '' or isinstance(dataset[row][col], str)): #sprawdzamy czy puste lub string
                dataset[row][col] = math.pi
    return dataset
 
## Funkcja zamienia puste wartosci/stringi numeryczne na losowe floaty/inty
#
def EmptyToRandom(dataset, start, stop, step):
    dataset = list(dataset)
    for row in range(len(dataset)):
        dataset[row] = list(dataset[row])
        for col in range(4, len(dataset[row])): #lecimy od 5ego, ponieważ poprzednie to faktyczne napisy
            if (isinstance(dataset[row][col], str)): #sprawdzamy czy puste lub string
                #dataset[row][col] = random.randint(0, int((stop - start) / step)) * step + start #generuje float
                dataset[row][col] = random.randint(start, stop)
    return dataset
 
def CiezkiSkrypt(dataset):
    dataset = list(dataset)
    for row in range(len(dataset)):
        dataset[row] = list(dataset[row])
        for col in range(len(dataset[row])):
            if(isinstance(dataset[row][col], (float, int))):
                dataset[row][col] = math.log(((dataset[row][col]**(1/float(3)) * math.sqrt(dataset[row][col]))**50) / round(dataset[row][col]**(1/float(3)) * math.sqrt(dataset[row][col])**50, 2))
    return dataset
 
#data = EmptyToPi(data)
data = EmptyToRandom(data, 1, 10, 1)
data = CiezkiSkrypt(data)
#print(data)

################################

dateend = datetime.datetime.now()
elapsedTime=dateend-datestart
totalTime+=elapsedTime
print(f"<br>Elapsed time (script execution): {elapsedTime}   (Started: {datestart}, Finished: {dateend})<br><br>")
print(f"Total time elapsed: {totalTime.strftime('%H:%M:%S.%f')}")
print("</div>\n</body>\n</html>")
