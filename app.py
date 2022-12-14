import sqlite3
import hashlib

conn = sqlite3.connect("DB_Cinemar.db")
cur = conn.cursor()
sql = """SELECT * FROM usuarios"""
cur.execute(sql)
res = cur.fetchall()
for i in res:
  print(i)
conn.close()

print("------------------")  #BORRAR ESTO AL TERMINAR

def registro(usuario,password,email,nombre,apellido):
  estado=0
  passEncryp = encriptar_contraseña(password)
  conn = sqlite3.connect("DB_Cinemar.db")
  cur = conn.cursor()
  sql = """INSERT INTO usuarios (usuario,
                              password,
                              email,
                              nombre,
                              apellido,
                              estado)
                        VALUES(?,?,?,?,?,?)"""
  cur.execute(sql,(usuario,passEncryp,email,nombre,apellido,estado))
  conn.commit()
  conn.close()
  return

def inicio_sesion(usuario,password):
  passEncryp = encriptar_contraseña(password)
  conn = sqlite3.connect("DB_Cinemar.db")
  cur = conn.cursor()
  sql = f"""SELECT * FROM usuarios WHERE usuario = ? AND password = ?"""
  cur.execute(sql,(usuario,passEncryp))
  res = cur.fetchall()
  print(res)
  conn.close()
  if res != []:
    print("Conexion Exitosa")
    return True
  else:
    print("Error de conexion")
    return False
  
  return

def crear_reserva(id_usuario,num_sala,pelicula,hora,fecha,butaca):
  conn = sqlite3.connect("DB_Cinemar.db")
  cur = conn.cursor()
  sql = """INSERT INTO reservas (id_usuario,
                              num_sala,
                              pelicula,
                              hora,
                              fecha,
                              butaca)
                        VALUES(?,?,?,?,?,?)"""
  cur.execute(sql,(id_usuario,num_sala,pelicula,hora,fecha,butaca))
  conn.commit()
  conn.close()

def mis_reserva():
  pass

def ver_reservas():
  pass

def historial():
  pass

def ver_reservas():
  pass

def consulta_reserva():
  pass

def crear_sala(num_sala,pelicula,tipo_sala,hora,fecha,cant_butacas):
  conn = sqlite3.connect("DB_Cinemar.db")
  cur = conn.cursor()
  sql = """INSERT INTO salas (num_sala,
                            pelicula,
                            tipo_sala,
                            hora,
                            fecha,
                            cant_butacas)
                     VALUES(?,?,?,?,?,?)"""
  cur.execute(sql,(num_sala,pelicula,tipo_sala,hora,fecha,cant_butacas))
  conn.commit()
  conn.close()
  return

def modificar_sala(id_sala,num_sala,pelicula,tipo_sala,hora,fecha,cant_butacas):
  conn = sqlite3.connect("DB_Cinemar.db")
  cur = conn.cursor()
  sql = f"""UPDATE salas SET num_sala = ?, 
                             pelicula = ?,
                             tipo_sala = ?,
                             hora = ?,
                             fecha = ?,
                             cant_butacas = ? 
                         WHERE  id_sala = ?"""
  cur.execute(sql,(num_sala,pelicula,tipo_sala,hora,fecha,cant_butacas,id_sala))
  conn.commit()
  conn.close()

def eliminar_sala(id_sala):
  conn = sqlite3.connect("DB_Cinemar.db")
  cur = conn.cursor()
  sql = f"""DELETE FROM salas WHERE id_sala = {id_sala} """
  cur.execute(sql)
  conn.commit()
  conn.close()
  return

def modificar_descuentos(dia,descuento):
  conn = sqlite3.connect("DB_Cinemar.db")
  cur = conn.cursor()
  sql = f"""UPDATE descuentos SET porcent_descuento = ? WHERE  dia = ?"""
  cur.execute(sql,(descuento,dia))
  conn.commit()
  conn.close()
  return

def ver_salas():
  conn = sqlite3.connect("DB_Cinemar.db")
  cur = conn.cursor()
  sql = """SELECT * FROM salas"""
  cur.execute(sql)
  res = cur.fetchall()
  for i in res:
    print(i)
  conn.commit()
  conn.close()
  return

def encriptar_contraseña(password):
  return hashlib.sha256(password.encode("utf-8")).hexdigest()
#-----------------------------------------------
#Ejecuciones Prueba
#
#registro("reproevo","1426","edu.onlyrock93@gmail.com","Patricio","Escobar")
#ver_salas()
#crear_sala(6,"Transformer","2D","14:30","14/06/2023",60)
#eliminar_sala(1)
#modificar_descuentos("Martes", 45 )
#crear_reserva(1,1,"Avatar","15:20","22-12-2022",7)
#modificar_sala(1,6,"Avatar","3D","15:30","22-12-2022",50)
#------------------------------------------------

def ver_descuentos():
  conn = sqlite3.connect("DB_Cinemar.db")
  cur = conn.cursor()
  sql = """SELECT * FROM descuentos"""
  cur.execute(sql)
  res = cur.fetchall()
  for i in res:
    print(i)
  conn.commit()
  conn.close()
  return

