#from __future__ import print_function
import mysql.connector

class baseDeDatos():

	def __init__(self):
		self.cnx= mysql.connector.connect(user='root',
			passwd='ATITA',
			host='localhost',
			database='facturacion')

		self.miCursor=cnx.cursor()

	def select_id_precio(self, id):
		sql = ("SELECT precioCrudo FROM productos WHERE id_producto = {}".format(id))

		try:
			self.miCursor.execute(sql)
			user = self.miscursor.fetchone()

		except Exception as e:
			raise

	def select_id_nombre(self,id):
		sql1 = ("SELECT nombre FROM productos WHERE id = {}".format(id))

		try:
			self.miCursor.execute(sql1)
			user1 =  self.micursor.fetchone()

		except Exception as e:
			raise




"""
#try:
cnx = mysql.connector.connect(user='root',
	passwd='ATITA',
	host='localhost',
	database='concesionario')

mycursor = cnx.cursor()
query = ("SELECT * FROM vendedores")

mycursor.execute(query)
result = mycursor.fetchall()

for i in result:
	print(i)

add_vendedor = ("INSERT INTO vendedores" 
					"(documento_vendedor, nombres, apellidos, ciudad)"
					"VALUES (%s,%s,%s,%s)")

data_vendedor = (('1968', 'Jorge', 'Riaño', 'Zipaquira'))



print("###############AGREGRA UN DATO###################")

mycursor.execute(add_vendedor,data_vendedor)
cnx.commit()

for i in mycursor:
	print(i)

cnx.close()

	cursor = cnx.cursor()

	query = ("SELECT * FROM vendedores")

	add_vendedor = ("INSERT INTO vendedores" 
					"(documento_vendedor, nombres, apellidos, ciudad)"
					"VALUES (%s,%s,%s,%s)")

	data_vendedor = ('1968', 'Jorge', 'Riaño', 'Zipaquira')

	cursor.execute(add_vendedor,data_vendedor)
	cursor.execute(query)

	print(cursor)

	cnx.commit()
	cursor.close()
	cnx.close()

except mysql.connector.Error as err:
	if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
		print("Something is wrong with your user name or password")
	elif err.errno == errorcode.ER_BAD_DB_ERROR:
		print("Database does not exist")
	else:
		print(err)
else:
	cnx.close()

"""












