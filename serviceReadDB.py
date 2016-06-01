import socket
import sqlite3, datetime
import time

d1p="unknown"
d1b1="unknown"
d1b2="unknown"
d1b3="unknown"

d2p="unknown"
d2b1="unknown"
d2b2="unknown"
d2b3="unknown"

d3p="unknown"
d3b1="unknown"
d3b2="unknown"
d3b3="unknown"

while True:


	conexion = sqlite3.connect("test.db")
	consulta = conexion.cursor()

	r = 1
	sql = "SELECT * FROM test WHERE id=%s" % r
	consulta.execute(sql)
	fila = consulta.fetchone()
	#print(("Seleccion del registro con ID %r: ") %(r, ))
	#print (fila[0], fila[1], fila[2], fila[3], fila[4], fila[5], fila[6], fila[7])
	#obtener piloto
	d1p=fila[1]
	#obtener valor baliza 1
	d1b1=fila[2]
	#obtener valor baliza 2
	d1b2=fila[3]
	#obtener valor baliza 3
	d1b3=fila[4]

	r = 2
	sql = "SELECT * FROM test WHERE id=%s" % r
	consulta.execute(sql)
	fila = consulta.fetchone()
	#print(("Seleccion del registro con ID %r: ") %(r, ))
	#print (fila[0], fila[1], fila[2], fila[3], fila[4], fila[5], fila[6], fila[7])
	#obtener piloto
	d2p=fila[1]
	#obtener valor baliza 1
	d2b1=fila[2]
	#obtener valor baliza 2
	d2b2=fila[3]
	#obtener valor baliza 3
	d2b3=fila[4]

	r = 3
	sql = "SELECT * FROM test WHERE id=%s" % r
	consulta.execute(sql)
	fila = consulta.fetchone()
	#print(("Seleccion del registro con ID %r: ") %(r, ))
	#print (fila[0], fila[1], fila[2], fila[3], fila[4], fila[5], fila[6], fila[7])
	#obtener piloto
	d3p=fila[1]
	#obtener valor baliza 1
	d3b1=fila[2]
	#obtener valor baliza 2
	d3b2=fila[3]
	#obtener valor baliza 3
	d3b3=fila[4]

	# dataDrone1="drone_1_piloto"+d1p+"drone_1_baliza_1"+d1b1+"drone_1_baliza_2"+d1b2+"drone_1_baliza_3"+d1b3
	# dataDrone2="drone_2_piloto"+d2p+"drone_2_baliza_1"+d2b1+"drone_2_baliza_2"+d2b2+"drone_2_baliza_3"+d2b3
	# dataDrone3="drone_3_piloto"+d3p+"drone_3_baliza_1"+d3b1+"drone_3_baliza_2"+d3b2+"drone_3_baliza_3"+d3b3

	#seq=(dataDrone1,dataDrone2,dataDrone3);
	seq=("d1p",d1p,"d1b1",d1b1,"d1b2",d1b2,"d1b3",d1b3,"d2p",d2p,"d2b1",d2b1,"d2b2",d2b2,"d2b3",d2b3,"d3p",d3p,"d3b1",d3b1,"d3b2",d3b2,"d3b3",d3b3);
	s=" ";	
	#print s.join( seq )
	#mensaje=s.join( seq )
	print s.join( seq )
	mensaje=s.join( seq )

	host='localhost'
	port=50000
	size=1024
	s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect((host,port))
	s.send(mensaje)
	#data=s.recv(size)
	s.close()
	
	time.sleep(2)
	#print 'Received:', data

