import serial
import pynmea2
import RPi.GPIO as GPIO
import socket
import sqlite3
import time
import os

GPIO.setmode(GPIO.BOARD)
GPIO.setup(12, GPIO.OUT)
GPIO.setup(16, GPIO.OUT)
GPIO.setup(18, GPIO.OUT)

#bd = os.path.dirname(__file__)+'\data\gps.db'
host = socket.gethostname()
con = sqlite3.connect("./data/gps.db")
cursor = con.cursor()

def parseGPS(str):
	if str.find('GGA') > 0:
		msg = pynmea2.parse(str,check=False)
		print "Timestamp: %s -- Lat: %s %s -- Lon: %s %s -- Senial: %s %s" % (msg.timestamp,msg.latitude,msg.lat_dir,msg.longitude,msg.lon_dir,msg.gps_qual,msg.num_sats)
		fecha = msg.timestamp
		id = host+fecha.strftime('%H%M%S')
		lat = msg.latitude
		long = msg.longitude
		q = msg.gps_qual

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
			id,fecha,lat,long,calidad_senial,enviado)
			values(?,?,?,?,?,0)
			"""
		]
		for sentencia in valores:
			cursor.execute(sentencia,[id,fecha.strftime('%H%M%S'),lat,long,q])
			#cursor.execute(sentencia,[id])
		con.commit()
		print('datos guardados')
		time.sleep(10)

serialPort = serial.Serial("/dev/ttyS0", 9600, timeout=0.5)

while True:
	str = serialPort.readline()
	parseGPS(str)

GPIO.output(12, False)
GPIO.output(16, False)
GPIO.output(18, False)


