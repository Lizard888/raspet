import datetime
import re
import calendar

import mysql.connector
from mysql.connector import Error

import pdb
import mysql.connector
#def bazad:
ur=[]
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

chasi=12
#cur.execute(query,den,chas)
#query = 'SELECT * FROM mondey WHERE chasi >="%s"' #работает
#cur.execute(query,chas)
#den="mondey"
#chas=12
nasden1=nomden+1
ur={}



query = ("SELECT * FROM %s" % den) #работает
cur.execute(query)
#query = 'SELECT * FROM %s % den WHERE chasi LIKE %s'
#cur.execute(query,chas)
print('den=',den)
for (n) in cur:
  kk1=n[1]
  kk2=n[2]
  kk3=n[3] 
  if kk2>=chasi:
     kk4=str(kk2)+"."+str(kk3)
     print(kk4,"  ",kk1)
     
     

   
