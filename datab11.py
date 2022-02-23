import datetime
import re
import calendar

import mysql.connector
from mysql.connector import Error

import pdb
import mysql.connector
#ld=["1"]
def bazad(ld):
 
  #global ld
  #print('ld=',ld)
  ur=[]
  now = datetime.datetime.now()



  ye=int(now.year)

  chas=int(now.hour)
  chas=10

  mi=int( now.minute)
  mi=19
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
#den=kalen.get(nomden)
  den="mondey"

  try:
    conn = mysql.connector.connect(
         user='root',
         #password='lizard',
         host='localhost',
         database='rasp')
    if conn.is_connected():
            print('Connected to MySQL database')

  except Error as e:
   print('e=',e)


  n=0
  cur = conn.cursor()
#pdb.set_trace() 

#chasi=chas
  chasi=12
  nasden1=nomden+1
  ur={}


  ld=[]
  query = ("SELECT * FROM %s" % den) #работает
  cur.execute(query)



  kkk1=[]
  kkk2=[]
  kkk3=[]

  print('den=',den)
  for (n) in cur:
    
    if n[2]>chasi:
        kkk2.append(n[2])
        kkk1.append(n[1])
        kkk3.append(n[3])
    
    
        
  print('ld=',ld)
  i=0

  kk=0
  i=0
  if abs(kkk3[0]-mi)>2:i=1
  while i!=len(kkk1):
     ld.append(kkk1[i])
     i=i+1

  print(ld)








   
