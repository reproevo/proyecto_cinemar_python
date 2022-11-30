import sqlite3

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
  conn = sqlite3.connect("DB_Cinemar.db")
  cur = conn.cursor()
  sql = """INSERT INTO usuarios (usuario,
                              password,
                              email,
                              nombre,
                              apellido,
                              estado)
                        VALUES(?,?,?,?,?,?)"""
  cur.execute(sql,(usuario,password,email,nombre,apellido,estado))
  conn.commit()
  conn.close()
  return

def inicio_sesion():
  pass

def crear_reserva():
  pass

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

def modificar_sala():
  pass

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
  sql = f"""UPDATE descuentos SET porcent_descuento = {descuento} WHERE  dia = '{dia}'"""
  cur.execute(sql)
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

#Ejecuciones Prueba

#registro("reproevo","1426","edu.onlyrock93@gmail.com","Patricio","Escobar")
#ver_salas()
#crear_sala(6,"Transformer","2D","14:30","14/06/2023",60)
#eliminar_sala(1)
#modificar_descuentos("Martes", 15 )

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

ver_descuentos()