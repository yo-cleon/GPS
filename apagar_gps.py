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

#from utils import archivoLog

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(12, GPIO.OUT)
GPIO.setup(16, GPIO.OUT)
GPIO.setup(18, GPIO.OUT)

#logger = archivoLog.getLogger()
#matricula = socket.gethostname()


GPIO.output(12, False)
GPIO.output(16, False)
GPIO.output(18, False)


#Conexión a la bbdd y creación del objeto cursor

#try:
	#con = sqlite3.connect("./data/gps.db")
	#cursor = con.cursor()
#except Exception as ex:
	#logger.error(ex)
	#print("Error: ")
	#print(ex)


