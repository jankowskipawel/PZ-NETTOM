#!/var/www/html/cgi-enabled/env/bin/python3
import pymysql
db = pymysql.connect(host='192.168.0.27',
                             user='root',
                             password='PzNettom2021!',
                             database='CSV_DB',
                             port=3306)