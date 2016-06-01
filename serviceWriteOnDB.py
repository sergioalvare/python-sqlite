import select
import socket
import sys
import sqlite3

db_name="maindb.db"

Variable_1_nombre="No_data"
Variable_2_nombre="No_data"
Variable_3_nombre="No_data"

Variable_1_valor="No_data"
Variable_2_valor="No_data"
Variable_3_valor="No_data"

host=''
port_sensor= 50008
port_nav= 8084
backlog=5
size=1024

#creo el servidor para atender a los clientes de las variables o sensores:
server_sensor=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_sensor.bind((host,port_sensor))
server_sensor.listen(backlog)
print("Servidor escuchando a sensores")

#meto los servidores y la entrada estandar en la lista input
input=[server_sensor,sys.stdin]

running=1
while running:
	print("Entrada en el bucle")
	inputready, outputready,exceptready=select.select(input,[],[])
	
	for s in inputready:
	#si llega un cliente sensor (if s==server_sensores), lo aniado a la lista de eventos a atender
		if s==server_sensor:
			client, address=server_sensor.accept()
			input.append(client)
	
	
	#si es un evento de teclado o en general de entrada estandar, corto el bucle
		elif s==sys.stdin:
			junk=sys.stdin.readline()
			running=0
	
	#si no es un servidor ni la entrada estandar, es un evento de cliente:
		else:
			print("Entrada en el else previo al recv")
			data=s.recv(size)
			if data: #si hay algo recibido
				print(data)
				#tupla = data.decode('utf8').split(" ")
				tupla = data.split(",")
				print(tupla)

				if "dronInfo" in data:
					#escribir cada dato recibido en el campo correspondiente
					conexion = sqlite3.connect(db_name)
					consulta = conexion.cursor()
					#create table drones(id varchar(60),piloto varchar(60),baliza1 varchar(60),baliza2 varchar(60),baliza3 varchar(60));
					identificadorDron=tupla[1]
					estadoBaliza1=tupla[2]
					estadoBaliza2=tupla[3]
					estadoBaliza3=tupla[4]

					consulta.execute("""UPDATE drones SET baliza1=%s, SET baliza2=%s, SET baliza3=%s WHERE id=%s""", (estadoBaliza1,estadoBaliza2,estadoBaliza3,identificadorDron));

				if "turretInfo" in data:
					#escribir cada dato recibido en el campo correspondiente
					conexion = sqlite3.connect(db_name)
					consulta = conexion.cursor()
					#create table torretas(drone_id varchar(60), contador_deteccion varchar(60), ruta_video varchar(60), contador_video varchar(60), ruta_foto varchar(60), contador_foto varchar(60));
					identificadorDronDetectado=tupla[1]
					VarContador_deteccion=tupla[2]
					VarRuta_video=tupla[3]
					VarContador_video=tupla[4]
					VarRuta_foto=tupla[5]
					VarContador_foto=tupla[6]

					#consulta.execute("UPDATE drones SET contador_deteccion=%s, SET ruta_video=%s, SET contador_video=%s, SET ruta_foto=%s, SET contador_foto=%s WHERE drone_id=%s", (	 VarContador_deteccion,VarRuta_video,VarContador_video,VarRuta_foto,VarContador_foto,identificadorDronDetectado));

					sentencia="UPDATE drones SET contador_deteccion="+VarContador_deteccion+", SET ruta_video="+VarRuta_video+", SET contador_video="+VarContador_video+", SET ruta_foto="+VarRuta_foto+", SET contador_foto="+VarContador_foto+"WHERE drone_id="+identificadorDronDetectado

					consulta.execute(sentencia);


					s.close()
					input.remove(s)
		
					
			else:
				s.close()
				input.remove(s)
			

#server_sensor.close()
#server_nav.close()



"""
if "ABCD" in "xxxxABCDyyyy":
    # whatever
"""
	
