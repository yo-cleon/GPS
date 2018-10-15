import logging

#Creacion y configuracion del log
LOG_FORMAT = "%(levelname)s: %(asctime)s -  %(message)s"
logging.basicConfig(filename = "./log/lecturas.log", level = logging.DEBUG, format = LOG_FORMAT)
logger = logging.getLogger()

def getLogger():
	return logger
