#programa cliente

import socket

#este sensor debe enviar "Variable_1_nombre nombre_de_la_variable Variable_1_valor valor_de_la_variable"

z = raw_input('Escribe numero de sensor de 1 a 3')
x = raw_input('Escribe nombre de la variable')
y = raw_input('Escribe valor numerico de la variable')
s = " ";
Variable_i_nombre="Variable_"+z+"_nombre"
Variable_i_valor="Variable_"+z+"_valor"
seq = (Variable_i_nombre, x, Variable_i_valor, y); # This is sequence of strings.
#seq = ("Variable_1_nombre", x, "Variable_1_valor", y); # This is sequence of strings.
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
#print 'Received:', data
