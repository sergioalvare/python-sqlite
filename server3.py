import select
import socket
import sys

Variable_1_nombre="No_data"
Variable_2_nombre="No_data"
Variable_3_nombre="No_data"

Variable_1_valor="No_data"
Variable_2_valor="No_data"
Variable_3_valor="No_data"


#cargar el index.html en un buffer:
f = open('index.html', 'r')
index_file_array=f.read()
print(index_file_array)

host=''
port_sensor= 50000
port_nav= 8084
backlog=5
size=1024

#creo el servidor para atender a los clientes de las variables o sensores:
server_sensor=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_sensor.bind((host,port_sensor))
server_sensor.listen(backlog)
print("Servidor escuchando a sensores")

#creo el servidor para el navegador:
server_nav=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_nav.bind((host,port_nav))
server_nav.listen(backlog)
print("Servidor escuchando a navegadores")

#meto los servidores y la entrada estandar en la lista input
input=[server_sensor,server_nav,sys.stdin]

running=1
while running:
	print("Entrada en el bucle")
	inputready, outputready,exceptready=select.select(input,[],[])
	
	for s in inputready:
	#si llega un cliente sensor (if s==server_sensores), lo aniado a la lista de eventos a atender
		if s==server_sensor:
			client, address=server_sensor.accept()
			input.append(client)
	#si llega un cliente de navegador (if s==server_navegadores), lo aniado a la lista de eventos a atender
		elif s==server_nav:
			print("Llegada de un navegador")
			client, address=server_nav.accept()
			#request = client.recv(1024)
			#print request
			input.append(client)
			#s.send(index_file_array)
	
	
	#si es un evento de teclado o en general de entrada estandar, corto el bucle
		elif s==sys.stdin:
			junk=sys.stdin.readline()
			running=0
	
	#si no es un servidor ni la entrada estandar, es un cliente:
		else:
			print("Entrada en el else previo al recv")
			data=s.recv(size)
			if data: #si hay algo recibido
			
				if "GET" in data: #si es un navegador
					print "Navegador conectado"
					client.send("HTTP/1.1 200 OK\n"+"Content-Type: text/html\n"+"\n"+"<html><body>Hello World</body></html>\n");
				#imprimir fichero al navegador, reemplazando las palabras clave por sus valores.
					index_file_array_temp=index_file_array.replace("Variable_1_nombre", Variable_1_nombre)
					index_file_array_temp=index_file_array_temp.replace("Variable_2_nombre", Variable_2_nombre)
					index_file_array_temp=index_file_array_temp.replace("Variable_3_nombre", Variable_3_nombre)
					index_file_array_temp=index_file_array_temp.replace("Variable_1_valor", Variable_1_valor)
					index_file_array_temp=index_file_array_temp.replace("Variable_2_valor", Variable_2_valor)
					index_file_array_temp=index_file_array_temp.replace("Variable_3_valor", Variable_3_valor)
					s.send(index_file_array_temp)
					s.close()
					input.remove(s)
			
		
				#si es un dato de cliente sensor, guardo el valor enviado en una variable
				else: 
					#el sensor envia "Variable_1_nombre nombre_de_la_variable Variable_1_valor valor_de_la_variable"
					print(data)
					tupla = data.split(" ")
					print(tupla)
				
					if "Variable_1_nombre" in data:
						Variable_1_nombre=tupla[1]
						Variable_1_valor=tupla[3]
				
					elif "Variable_2_nombre" in data:
						Variable_2_nombre=tupla[1]
						Variable_2_valor=tupla[3]
				
					else:
						Variable_3_nombre=tupla[1]
						Variable_3_valor=tupla[3]
				
					
			else:
				s.close()
				input.remove(s)
			
	#si es un dato de cliente navegador, abro el fichero index.html, lo guardo en un buffer,
	#reemplazo las variables por los valores que tenga almacenados para ellas, y
	#finalmente imprimo el fichero en el socket del navegador

#server_sensor.close()
#server_nav.close()





"""


if "ABCD" in "xxxxABCDyyyy":
    # whatever


"""
	