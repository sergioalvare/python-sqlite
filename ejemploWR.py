import select
import socket
import sys
import sqlite3

db_name="maindb.db"

con=sqlite3.connect(db_name)
cursor=con.cursor()

VarContador_deteccion="AAAA"
VarRuta_video="BBBB"
VarContador_video="CCCC"
VarRuta_foto="DDDD"
VarContador_foto="EEEE"
identificadorDronDetectado="2"

#solicitud="UPDATE torretas SET contador_deteccion="+VarContador_deteccion+", ruta_video="+VarRuta_video+", contador_video="+VarContador_video+", ruta_foto="+VarRuta_foto+", contador_foto="+VarContador_foto+" WHERE id="+identificadorDronDetectado

#solicitud="UPDATE torretas SET contador_deteccion="+VarContador_deteccion+" WHERE id="+identificadorDronDetectado

#solicitud="UPDATE torretas SET contador_deteccion='prueba4' WHERE id='2'"


cursor.execute("""UPDATE torretas SET contador_deteccion = ? WHERE drone_id= ? """,
  (VarContador_deteccion,identificadorDronDetectado))

#cursor.execute("UPDATE torretas set contador_deteccion = 25000.00 where id=1")


#print(solicitud)

#cursor.execute(solicitud);
con.commit()

