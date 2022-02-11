import datetime
import re
import calendar

import mysql.connector
from mysql.connector import Error

import pdb
import mysql.connector
#global ld
#ld=[]
#global ld
def bazad(ld):
 
  ur=[]
  now = datetime.datetime.now()



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

  chasi=chis

  nasden1=nomden+1
  #ur={}


  
  query = ("SELECT * FROM %s" % den) #работает
  cur.execute(query)

  print('den=',den)
  for (n) in cur:
    kk1=n[1]
    kk2=n[2]
    kk3=n[3] 
    if kk2>=chasi:
     kk4=str(kk2)+"."+str(kk3)
     print(kk4,"  ",kk1)
     kk5=kk4+"  "+kk1
     ld.append(kk5)
     

  print(ld)

   
