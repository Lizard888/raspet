import telebot
import configparser
import json
from telebot import apihelper
import datetime
import re
import calendar
from datab1 import bazad
ld=[]
Token1="948381879:AAEO07_DU1z-CO67NRWIi8HX_jeLNfQVqPo" #Totochka
bot = telebot.TeleBot(Token1)
@bot.message_handler(commands=['start'])
def start_command(message):

   bazad(ld)
   i=0
   for (i) in  ld:
         bot.send_message(  message.chat.id,i)
         print(i)
bot.polling()
