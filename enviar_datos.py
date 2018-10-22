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
		"mat" :data[0],
		"lat" :data[1],
 		"long":data[2]
	}
with open('lecturas.json','w') as file:
	json.dump(datos, file)


#enviamos la petición al servidor REST
url = 'http://gestiomar2.dyndns.biz:8881/gps'
#with open("lecturas.json","r") as file:
#	datos = json.load(file)

datos = {"lat": 28.493466666666666, "mat": "0324-BLD", "long": -16.32621}
print("Datos a enviar:")
print(datos)
r = requests.post(url,datos)
print(r.status_code)
if (r.status_code == 200):
	print("Datos enviados")
print(r.text)
