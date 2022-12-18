import sqlite3
import hashlib
from datetime import *

def listar_usuarios():
  conn = sqlite3.connect("DB_Cinemar.db")
  cur = conn.cursor()
  sql = """SELECT * FROM usuarios"""
  cur.execute(sql)
  res = cur.fetchall()
  conn.close()
  return res

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

def registroAdm(usuario,password,email,nombre,apellido,estado):
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

def editarUsuarioAdm(id,usuario,password,email,nombre,apellido,estado):
  conn = sqlite3.connect("DB_Cinemar.db")
  cur = conn.cursor()
  sql = """UPDATE usuarios SET  usuario = ?, 
                             password = ?,
                             email = ?,
                             nombre = ?,
                             apellido = ?,
                             estado = ? 
                         WHERE  id = ?"""
  cur.execute(sql,(usuario,password,email,nombre,apellido,estado,id))
  conn.commit()
  conn.close()

def disponibilidad(usuario):
  conn = sqlite3.connect("DB_Cinemar.db")
  cur = conn.cursor()
  sql = """SELECT * FROM usuarios WHERE usuario = ?"""
  cur.execute(sql,(usuario,))
  res = cur.fetchall()
  conn.close()
  if res == []:
    print("Nombre de Usuario Disponible")
    return True
  else:
    print("Nombre de Usuario OCUPADO")
    res = [] #vacio la variable que guardo la consulta con los datos obtenidos de la BD
    return False

def inicio_sesion(usuario,password):
  passEncryp = encriptar_contraseña(password)
  conn = sqlite3.connect("DB_Cinemar.db")
  cur = conn.cursor()
  sql = """SELECT * FROM usuarios WHERE usuario = ? AND password = ?"""
  cur.execute(sql,(usuario,passEncryp))
  res = cur.fetchall()
  conn.close()
  if res != []:
    return True,res
  else:
    return False

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

def mis_reserva(id_usuario):
  hoy = datetime.today()
  conn = sqlite3.connect("DB_Cinemar.db")
  cur = conn.cursor()
  sql = """SELECT * FROM reservas WHERE id_usuario = ? AND fecha > ?"""
  cur.execute(sql,(id_usuario,hoy))
  conn.close()
  res = cur.fetchall()
  
def ver_reservas():
  conn = sqlite3.connect("DB_Cinemar.db")
  cur = conn.cursor()
  sql = """SELECT * FROM reservas"""
  cur.execute(sql,)
  res = cur.fetchall()
  conn.close()
  return res

def historial(id_usuario):
  conn = sqlite3.connect("DB_Cinemar.db")
  cur = conn.cursor()
  sql = """SELECT * FROM reservas WHERE id_usuario = ?"""
  cur.execute(sql,(id_usuario))
  conn.close()

def consultar_usuario(id_usuario):
  conn = sqlite3.connect("DB_Cinemar.db")
  cur = conn.cursor()
  sql = """SELECT * FROM usuarios WHERE id = ?"""
  cur.execute(sql,(id_usuario,))
  res = cur.fetchall()
  conn.close()
  return res

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

def modificar_descuentos(id,descuento):
  conn = sqlite3.connect("DB_Cinemar.db")
  cur = conn.cursor()
  sql = f"""UPDATE descuentos SET porcent_descuento = ? WHERE  id_descuentos = ?"""
  cur.execute(sql,(descuento,id))
  conn.commit()
  conn.close()


def ver_salas():
  conn = sqlite3.connect("DB_Cinemar.db")
  cur = conn.cursor()
  sql = """SELECT * FROM salas"""
  cur.execute(sql)
  res = cur.fetchall()
  conn.commit()
  conn.close()
  return(res)

def consultar_sala(id):
  conn = sqlite3.connect("DB_Cinemar.db")
  cur = conn.cursor()
  sql = """SELECT * FROM salas WHERE id_sala = ?"""
  cur.execute(sql,(id,))
  res = cur.fetchall()
  conn.commit()
  conn.close()
  return(res)

def ver_descuentos():
  conn = sqlite3.connect("DB_Cinemar.db")
  cur = conn.cursor()
  sql = """SELECT * FROM descuentos"""
  cur.execute(sql)
  res = cur.fetchall()
  conn.commit()
  conn.close()
  return res

def consultar_descuentos(id):
  conn = sqlite3.connect("DB_Cinemar.db")
  cur = conn.cursor()
  sql = """SELECT * FROM descuentos WHERE id_descuentos = ?"""
  cur.execute(sql,(id,))
  res = cur.fetchall()
  conn.commit()
  conn.close()
  return res

def encriptar_contraseña(password):
  return hashlib.sha256(password.encode("utf-8")).hexdigest()
#-----------------------------------------------
#Ejecuciones Prueba
#
#registro("edu","1234","edu@gmail.com","Patricio","Escobar")
#listar_usuarios()
#ver_salas()
#crear_sala(6,"Transformer","2D","14:30","14/06/2023",60)
#eliminar_sala(1)
#modificar_descuentos("Martes", 45 )
#crear_reserva(1,1,"Avatar","15:20","22-12-2022",7)
#modificar_sala(1,6,"Avatar","3D","15:30","22-12-2022",50)
#print(inicio_sesion("edu","1234")[1][0][6])
#disponibilidad("edu")
#------------------------------------------------