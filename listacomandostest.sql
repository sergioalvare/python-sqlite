sqlite3 maindb.db

create table drones(id varchar(60),piloto varchar(60),baliza1 varchar(60),baliza2 varchar(60),baliza3 varchar(60));
create table usuarios (NOM_USU varchar(60), APE_USU varchar(60), EMA_USU varchar(60), IMA_USU varchar(60), ID_USU varchar(60));
create table torretas(drone_id varchar(60), contador_deteccion varchar(60), ruta_video varchar(60), contador_video varchar(60), ruta_foto varchar(60), contador_foto varchar(60));


INSERT INTO drones VALUES('1', 'unknown','no','yes','no');
INSERT INTO drones VALUES('2', 'unknown','no','yes','yes');
INSERT INTO drones VALUES('3', 'unknown','yes','yes','no');

INSERT INTO usuarios VALUES('Señor', 'biceps','señor@biceps.com','personaje.png','aliasseñorbiceps');

INSERT INTO torretas VALUES('2', 'unknown', 'unknown', 'unknown', 'unknown', 'unknown');

.quit

