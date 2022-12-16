import sqlite3
import hashlib
from datetime import *

def listar_usuarios():
  conn = sqlite3.connect("DB_Cinemar.db")
  cur = conn.cursor()
  sql = """SELECT * FROM usuarios"""
  cur.execute(sql)
  res = cur.fetchall()
  for i in res:
    print(i)
  conn.close()

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

def disponibilidad(usuario):
  conn = sqlite3.connect("DB_Cinemar.db")
  cur = conn.cursor()
  sql = """SELECT * FROM usuarios WHERE usuario = ?"""
  cur.execute(sql,(usuario,))
  res = cur.fetchall()
  print(res)
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
    print("Conexion Exitosa")
    return True,res
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
  conn.close()

def historial(id_usuario):
  conn = sqlite3.connect("DB_Cinemar.db")
  cur = conn.cursor()
  sql = """SELECT * FROM reservas WHERE id_usuario = ?"""
  cur.execute(sql,(id_usuario))
  conn.close()

def consultar_reservas():
  conn = sqlite3.connect("DB_Cinemar.db")
  cur = conn.cursor()
  sql = """SELECT * FROM reservas WHERE fecha > ?"""
  cur.execute(sql,)
  conn.close()

def consultar_usuario(id_usuario):
  conn = sqlite3.connect("DB_Cinemar.db")
  cur = conn.cursor()
  sql = """SELECT * FROM usuarios WHERE id_usuario = ?"""
  cur.execute(sql,(id_usuario))
  conn.close()

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

def modificar_descuentos(dia,descuento):
  conn = sqlite3.connect("DB_Cinemar.db")
  cur = conn.cursor()
  sql = f"""UPDATE descuentos SET porcent_descuento = ? WHERE  dia = ?"""
  cur.execute(sql,(descuento,dia))
  conn.commit()
  conn.close()

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

def encriptar_contraseña(password):
  return hashlib.sha256(password.encode("utf-8")).hexdigest()