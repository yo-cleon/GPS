# /usr/bin/python
# -*- coding: utf-8 -*-

import json
import requests
import sqlite3

#conexion a la bbdd y obtención del útimo regristro
bd = './data/gps.db'
con = sqlite3.connect(bd)
cursor = con.cursor()
q = cursor.execute('select matricula, lat, long from lecturas order by ID desc limit 0,1 ')

#generamos un archivo json para enviarlo al servidor
for data in q.fetchall():
	datos = {
		'matricula':data[0],
		'latitud':data[2],
 		'longitud':data[1]
	}
print (data)
#with open('lecturas.json','w') as file:
#	json.dump(datos, file)

#enviamos la petición al servidor REST
url = 'http://192.168.1.19:8881/gps'
#with open("lecturas.json","r") as file:
#	datos = json.load(file)

print("Datos a enviar:")
print(datos)
#Envio de datos al servidor rest
r = requests.post(url, json=datos)
print(r.status_code)
if (r.status_code == 200):
	print("Datos enviados")
print(r.text)
