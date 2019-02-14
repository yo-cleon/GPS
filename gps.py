#! /usr/bin/python
# -*- coding: utf-8 -*-

import commands
import datetime
import pynmea2
import os
import RPi.GPIO as GPIO
import serial
import socket
import sqlite3
import time

from utils import archivoLog

GPIO.setmode(GPIO.BOARD)
GPIO.setup(12, GPIO.OUT)
GPIO.setup(16, GPIO.OUT)
GPIO.setup(18, GPIO.OUT)

logger = archivoLog.getLogger()
matricula = socket.gethostname()

#Conexión a la bbdd y creación del objeto cursor
try:
	con = sqlite3.connect("./data/gps.db")
	cursor = con.cursor()
except Exception as ex:
	logger.error(ex)
	print("Error: ")
	print(ex)

cursor.execute("SELECT max(id) from LECTURAS")
id = cursor.fetchone()[0]
if id != 0:
	id += 1

else:
	id = 1

def parseGPS(str):
	if str.find('GGA') > 0:
		global id
		msg = pynmea2.parse(str,check=False)
		fecha = datetime.datetime.now().strftime("%Y%m%d")
		hora = datetime.datetime.now().strftime("%H%M%S")
		lat = msg.latitude
		long = msg.longitude
		q = msg.gps_qual
		print ("Timestamp: %s --FECHA: %s -- HORA: %s -- Lat: %s %s -- Lon: %s %s -- Senial: %s %s" % (msg.timestamp, fecha,hora,msg.latitude,msg.lat_dir,msg.longitude,msg.lon_dir,msg.gps_qual,msg.num_sats))

		if q == 0:
			GPIO.output(12, True)
			GPIO.output(16, False)
			GPIO.output(18, False)
		elif q == 1:
			GPIO.output(16, True)
			GPIO.output(12, False)
			GPIO.output(18, False)
		else:
			GPIO.output(18, True)
			GPIO.output(12, False)
			GPIO.output(16, False)
		valores = [
			"""
			Insert into LECTURAS (
			id,matricula,fecha,hora,lat,long,calidad_senial,enviado)
			values(?,?,?,?,?,?,?,0)
			"""
		]

		try:

			for sentencia in valores:
				cursor.execute(sentencia,[id,matricula,fecha,hora,lat,long,q])
			con.commit()
			print("Datos guardados")
			id = id + 1
			result = commands.getoutput('/usr/bin/python ./enviar_datos.py')
			print("Datos enviados")
		except Exception as ex:
			logger.warning(ex)
			print('Error al escribir en la bbdd: ')
			print(ex)
			pass
		time.sleep(10)

serialPort = serial.Serial("/dev/ttyS0", 9600, timeout=0.5)

while True:
	try:
		str = serialPort.readline()
		parseGPS(str)
	except Exception as ex:
		logger.warning(ex)
		print ('Error:')
		print(ex)
		pass

GPIO.output(12, False)
GPIO.output(16, False)
GPIO.output(18, False)


