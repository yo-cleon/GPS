import json
import sqlite3

bd = './data/gps.db'
con = sqlite3.connect(bd)
cursor = con.cursor()

q = cursor.execute('select id, lat, long from lecturas order by id ')
for data in q.fetchall():
	datos = {
		'id ' : data[0],
		'lat' :  data[1],
 		'long' :  data[2]
	}
with open('lecturas.json','w') as file:
	json.dump(datos, file)
