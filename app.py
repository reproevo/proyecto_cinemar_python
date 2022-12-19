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

def eliminarUsuario(id):
  estado=3
  conn = sqlite3.connect("DB_Cinemar.db")
  cur = conn.cursor()
  sql = """UPDATE usuarios SET  estado = ? WHERE  id = ?"""
  cur.execute(sql,(estado,id))
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
    #print("Nombre de Usuario Disponible")
    return True
  else:
    #print("Nombre de Usuario OCUPADO")
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

def crear_reserva(usuario,num_sala,pelicula,tipo_sala,hora,fecha,id_sala):
  conn = sqlite3.connect("DB_Cinemar.db")
  cur = conn.cursor()
  sql = """INSERT INTO reservas (usuario,
                            num_sala,
                            pelicula,
                            tipo_sala,
                            hora,
                            fecha,
                            id_sala)
                     VALUES(?,?,?,?,?,?,?)"""
  cur.execute(sql,(usuario,num_sala,pelicula,tipo_sala,hora,fecha,id_sala))
  conn.commit()
  conn.close()

def eliminar_reserva(usuario,id):
  conn = sqlite3.connect("DB_Cinemar.db")
  cur = conn.cursor()
  sql = """DELETE FROM reservas WHERE usuario = ?
                                AND id_reserva = ?"""
  cur.execute(sql,(usuario,id))
  conn.commit()
  conn.close()

def mis_reservas(usuario):
  hoy = datetime.today()
  fecha = hoy.strftime('%d-%m-%Y')
  #hora = hoy.strftime("%H:%M")
  conn = sqlite3.connect("DB_Cinemar.db")
  cur = conn.cursor()
  sql = """SELECT * FROM reservas WHERE usuario = ? AND fecha > ?"""
  cur.execute(sql,(usuario,fecha))
  res = cur.fetchall()
  conn.close()
  return res 

def mi_historial(usuario):
  hoy = datetime.today()
  fecha = hoy.strftime("%d-%m-%Y")
  #hora = hoy.strftime("%H:%M")
  conn = sqlite3.connect("DB_Cinemar.db")
  cur = conn.cursor()
  sql = """SELECT * FROM reservas WHERE usuario = ? AND fecha < ?"""
  cur.execute(sql,(usuario,fecha))
  res = cur.fetchall()
  conn.close()
  return res

def ver_reservas():
  conn = sqlite3.connect("DB_Cinemar.db")
  cur = conn.cursor()
  sql = """SELECT * FROM reservas"""
  cur.execute(sql,)
  res = cur.fetchall()
  conn.close()
  return res

def ver_reservasParticular(id):
  usuario = consultar_usuario(id)[0][1]
  conn = sqlite3.connect("DB_Cinemar.db")
  cur = conn.cursor()
  sql = """SELECT * FROM reservas WHERE usuario = ? """
  cur.execute(sql,(usuario,))
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
  sql = """SELECT porcent_descuento FROM descuentos WHERE id_descuentos = ?"""
  cur.execute(sql,(id,))
  res = cur.fetchall()
  conn.commit()
  conn.close()
  return res

def consultar_diadescuentos(id):
  conn = sqlite3.connect("DB_Cinemar.db")
  cur = conn.cursor()
  sql = """SELECT dia FROM descuentos WHERE id_descuentos = ?"""
  cur.execute(sql,(id,))
  res = cur.fetchall()
  conn.commit()
  conn.close()
  return res

def consultarDia():
  hoy = datetime.now()
  dia = hoy.weekday()+1
  return dia

def consultarDescuentoVip(id):
  estado = consultar_usuario(id)[0][6]
  if estado == 4:
    id_dia = consultarDia()
    val_desc = consultar_descuentos(id_dia)[0][0]
  elif estado ==0:
    val_desc = 0
  else:
    print("estado no valido")
  return val_desc

def encriptar_contraseña(password):
  return hashlib.sha256(password.encode("utf-8")).hexdigest()

def precios(formato):
  conn = sqlite3.connect("DB_Cinemar.db")
  cur = conn.cursor()
  sql = """SELECT * FROM tarifas WHERE tipo_sala = ?"""
  cur.execute(sql,(formato,))
  res = cur.fetchall()
  conn.commit()
  conn.close()
  return res

def calcularPrecio(formato,descuento):
  preciototal = precios(formato)[0][2]
  pagar = preciototal - (preciototal * descuento)/100
  return pagar

def disponibilidadSala(id):
  sala = consultar_sala(id)
  cantidad = consultar_reservasSala(sala[0][0])
  if len(cantidad) < sala[0][6]:
    return True
  else:
    return False

def consultar_reservasSala(id):
  conn = sqlite3.connect("DB_Cinemar.db")
  cur = conn.cursor()
  sql = """SELECT * FROM reservas WHERE id_sala = ?"""
  cur.execute(sql,(id,))
  res = cur.fetchall()
  conn.close()
  return res


#-----------------------------------------------
#Ejecuciones Prueba
#
#registro("edu","1234","edu@gmail.com","Patricio","Escobar")
#listar_usuarios()
#ver_salas()
#crear_sala(6,"Transformer","2D","14:30","14/06/2023",60)
#eliminar_sala(1)
#modificar_descuentos("Martes", 45 )
#crear_reserva("1234",1,"Avatar","3D","15:20","22-12-2022",7)
#modificar_sala(1,6,"Avatar","3D","15:30","22-12-2022",50)
#print(inicio_sesion("edu","1234")[1][0][6])
#disponibilidad("edu")
#print(consultarDescuentoVip(6))
# print(precios("2D")[0][2])
# print(calcularPrecio("2D",50))
#disponibilidadSala(4)
#------------------------------------------------