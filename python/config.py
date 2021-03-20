#!/var/www/html/cgi-enabled/env/bin/python3
import pymysql
from MySQLdb import _mysql
db = pymysql.connect(host='192.168.0.27',
                             user='root',
                             password='PzNettom2021!',
                             database='CSV_DB',
                             port=3306)

db_mysqldb=_mysql.connect(host="192.168.0.27",user="root",
                  passwd="PzNettom2021!",db="CSV_DB")