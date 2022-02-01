import datetime
import re
import calendar

import mysql.connector
from mysql.connector import Error

import pdb
import mysql.connector
#def bazad:

now = datetime.datetime.now()

#@bot.message_handler(commands=['start'])

ye=int(now.year)
print(ye)
chas=int(now.hour)
min=int( now.minute)
print('chas=',chas)
print('min=',min)
mes=int(now.month)
chis=int(now.day)

post=0
nomden=calendar.weekday(ye,mes,chis)
#print('nomden=',nomden)
kalen={}
kalen={0:"mondey",
         1:"tuesday",
         2:"wednesday",
         3:"thursday",
         4:"friday"}
den=kalen.get(nomden)

try:
   conn = mysql.connector.connect(
         user='root',
         #password='lizard',
         host='localhost',
         database='rasp')
   if conn.is_connected():
            print('Connected to MySQL database')

except Error as e:
        print(e)


n=0
cur = conn.cursor()
#pdb.set_trace() 
#query="SELECT * FROM %s WHERE chasi LIKE \"%" + chas +"%\" "
#query = 'SELECT * FROM "%s" WHERE chasi LIKE "%s"'
#cur.execute(sql, (us,))
chasi=12
#cur.execute(query,den,chas)
#query = 'SELECT * FROM mondey WHERE chasi >="%s"' работает
#cur.execute(query,chas)
#den="mondey"
chas=12
nasden1=nomden+1
#query = 'SELECT nasden FROM dnined'

#query = 'SELECT * FROM den WHERE chasi >="%s"'
#cur.execute(query,chas)

query = ("SELECT * FROM %s" % den)
cur.execute(query)
print('den=',den)
for (n) in cur:
  print(n)
    
