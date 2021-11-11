# Importar Bibliotecas
from sqlite3.dbapi2 import Date, Error
from tkinter import *
from tkinter import messagebox
from tkinter import ttk 
import sqlite3
from tkcalendar import Calendar,DateEntry
import datetime 
from datetime import date, timedelta

#from sqlite3 import Error
#import traceback
#import sys

# Desarrollo de la Interfaz grafica
root=Tk()
root.title("Generacion Stickers BELCORP")
root.geometry("800x600")

miId=StringVar()
miSolicitud=StringVar()
miAviso=StringVar()
miFormula=StringVar()
miDescripcion=StringVar()
miFechaIngreso=StringVar()
miTipo=StringVar()
miTiempo=StringVar()
miTemperatura=StringVar()
miCantFQ=StringVar()
miCantMB=StringVar()
miCantPreservantes=StringVar()
miCantContraMuestra=StringVar()
miFechaMuestra=StringVar()

miTiempo.set('0')

def conexionBBDD():
	miConexion=sqlite3.connect("base.db")
	miCursor=miConexion.cursor()

# ''' 
#             DESCRIPCION VARCHAR(50),
#             FECHAINGRESO DATE,
#             TIPO VARCHAR(50),
#             TIEMPO INTEGER,
#             TEMPERATURA INTEGER,
#             CANTFQ VARCHAR(50),
#             CANTPRESERVANTES VARCHAR(50),
#             CANTCONTRAMUESTRA VARCHAR(50),
#             FECHAMUESTRA VARCHAR(50) '''

	try:
		miCursor.execute('''
			
			CREATE TABLE IF NOT EXISTS tblDatos (
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            SOLICITUD INTEGER NOT NULL,
            AVISO INTEGER NOT NULL,
			FORMULA VARCHAR(50) NOT NULL,
			DESCRIPCION VARCHAR(50),
			FECHAINGRESO DATE,
			TIPO VARCHAR(50),
			TIEMPO INTEGER NOT NULL,
			TEMPERATURA INTEGER NOT NULL,
			CANTFQ VARCHAR(50),
			CANTMB VARCHAR(50),
			CANTPRESERVANTES VARCHAR(50),
            CANTCONTRAMUESTRA VARCHAR(50),
			FECHAMUESTRA VARCHAR(50)
			)


			''')
		miCursor.execute('''
			
			CREATE TABLE IF NOT EXISTS tblStickers (
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            SOLICITUD INTEGER NOT NULL,
            AVISO INTEGER NOT NULL,
			FORMULA VARCHAR(50) NOT NULL,
			DESCRIPCION VARCHAR(50),
			FECHAINGRESO DATE,
			TIPO VARCHAR(50),
			TIEMPO INTEGER NOT NULL,
			TEMPERATURA INTEGER NOT NULL,
			CANTFQ VARCHAR(50),
			CANTMB VARCHAR(50),
			CANTPRESERVANTES VARCHAR(50),
            CANTCONTRAMUESTRA VARCHAR(50),
			FECHAMUESTRA VARCHAR(50)
			)


			''')
		messagebox.showinfo("CONEXION","Base de Datos Creada exitosamente")
	except:
		messagebox.showinfo("CONEXION", "Conexión con la base de datos ERRONEA")

def eliminarBBDD():
	miConexion=sqlite3.connect("base.db")
	miCursor=miConexion.cursor()
	if messagebox.askyesno(message="¿Los Datos se perderan definitivamente, Desea continuar?", title="ADVERTENCIA"):
		miCursor.execute("DROP TABLE tblDatos")
	else:
		pass
	#messagebox.showinfo("CONEXION", "Conexión con la base de datos ERRONEA")
	limpiarCampos()
	mostrar()

def salirAplicacion():
	valor=messagebox.askquestion("Salir","¿Está seguro que desea salir de la Aplicación?")
	if valor=="yes":
		root.destroy()

def limpiarCampos():
	miId.set("")
	miSolicitud.set("")
	miAviso.set("")
	miFormula.set("")
	miDescripcion.set("")
	miFechaIngreso.set("")
	miTipo.set("")
	miTiempo.set("0")
	miTemperatura.set("")
	miCantFQ.set("")
	miCantMB.set("")
	miCantPreservantes.set("")
	miCantContraMuestra.set("")
	miFechaMuestra.set("")

def mensaje():
	acerca='''
	Generador de Stickers
	Version 1.0
	Tecnología Python Tkinter
	'''
	messagebox.showinfo(title="INFORMACION", message=acerca)

################################ Métodos CRUD ##############################

def crear():
	miConexion=sqlite3.connect("base.db")
	miCursor=miConexion.cursor()
	try:
		datos=miSolicitud.get(),miAviso.get(),miFormula.get(),miDescripcion.get(),miFechaIngreso.get(),miTipo.get(),miTiempo.get(),miTemperatura.get(),miCantFQ.get(),miCantMB.get(),miCantPreservantes.get(),miCantContraMuestra.get(),miFechaMuestra.get()
		miCursor.execute('INSERT INTO tblDatos VALUES(NULL, ?, ?, ?, ?, ?, ?, ?, ?, ? ,? ,? ,? ,?)', (datos))

		CantFQ = 0
		CantMB = 0
		CantPreservantes = 0
		CantContraMuestra = 0

		for registro in range(int(miCantFQ.get())):
    			CantFQ = CantFQ + 1
    			sticker=miSolicitud.get(),miAviso.get(),miFormula.get(),miDescripcion.get(),miFechaIngreso.get(),miTipo.get(),miTiempo.get(),miTemperatura.get(),CantFQ,miCantPreservantes.get(),miCantContraMuestra.get(),miFechaMuestra.get()
    			print(sticker)
    			#miCursor.execute('INSERT INTO tblStickers VALUES(NULL, ?, ?, ?, ?, ?, ?, ?, ?, ? ,? , ? , ?)', (sticker))
		
		for registro in range(int(miCantFQ.get())):
    			CantMB = CantMB + 1
    			sticker=miSolicitud.get(),miAviso.get(),miFormula.get(),miDescripcion.get(),miFechaIngreso.get(),miTipo.get(),miTiempo.get(),miTemperatura.get(),miCantFQ.get(),CantMB,miCantPreservantes.get(),miCantContraMuestra.get(),miFechaMuestra.get()
    			print(sticker)
    			#miCursor.execute('INSERT INTO tblStickers VALUES(NULL, ?, ?, ?, ?, ?, ?, ?, ?, ? ,? , ? , ?)', (sticker))

		for registro in range(int(miCantPreservantes.get())):
    			CantPreservantes = CantPreservantes + 1
    			sticker=miSolicitud.get(),miAviso.get(),miFormula.get(),miDescripcion.get(),miFechaIngreso.get(),miTipo.get(),miTiempo.get(),miTemperatura.get(),miCantFQ.get(),miCantMB.get(),CantPreservantes,miCantContraMuestra.get(),miFechaMuestra.get()
    			print(sticker)
    			#miCursor.execute('INSERT INTO tblStickers VALUES(NULL, ?, ?, ?, ?, ?, ?, ?, ?, ? ,? , ? , ?)', (sticker))
		
		for registro in range(int(miCantContraMuestra.get())):
    			CantContraMuestra = CantContraMuestra + 1
    			sticker=miSolicitud.get(),miAviso.get(),miFormula.get(),miDescripcion.get(),miFechaIngreso.get(),miTipo.get(),miTiempo.get(),miTemperatura.get(),miCantFQ.get(),miCantMB.get(),miCantPreservantes.get(),CantContraMuestra,miFechaMuestra.get()
    			print(sticker)
    			#miCursor.execute('INSERT INTO tblStickers VALUES(NULL, ?, ?, ?, ?, ?, ?, ?, ?, ? ,? , ? , ?)', (sticker))
		miConexion.commit()

	 
	except Error:
		messagebox.showwarning("ADVERTENCIA","Ocurrió un error al crear el registro, verifique conexión con BBDD")
		print(datos)
		print(Error)
	pass
	limpiarCampos()
	mostrar()

def mostrar():
	miConexion=sqlite3.connect("base.db")
	miCursor=miConexion.cursor()
	registros=tree.get_children()
	for elemento in registros:
		tree.delete(elemento)

	try:
		miCursor.execute("SELECT * FROM tblDatos")
		for row in miCursor:
			tree.insert("",0,text=row[0], values=(row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10],row[11],row[12]))
	except:
		pass

                ################################## Tabla ################################
tree=ttk.Treeview(height=10, columns=('#0','#1','#2','#3','#4','#5','#6','#7','#8','#9','#10','#11','#12','#13'))
tree.place(x=20, y=340)

tree.column('#0',width=40)
tree.heading('#0', text="ID", anchor=CENTER)
tree.column('#1',width=40)
tree.heading('#1', text="Solicitud", anchor=CENTER)
tree.column('#2',width=40)
tree.heading('#2', text="Aviso", anchor=CENTER)
tree.column('#3',width=40)
tree.heading('#3', text="Formula", anchor=CENTER)
tree.column('#4',width=40)
tree.heading('#4', text="Descripcion", anchor=CENTER)
tree.column('#5',width=40)
tree.heading('#5', text="FechaIngreso", anchor=CENTER)
tree.column('#6',width=40)
tree.heading('#6', text="Tipo", anchor=CENTER)
tree.column('#7',width=40)
tree.heading('#7', text="Tiempo", anchor=CENTER)
tree.column('#8',width=40)
tree.heading('#8', text="Temperatura", anchor=CENTER)
tree.column('#9',width=40)
tree.heading('#9', text="CantFQ", anchor=CENTER)
tree.column('#10',width=40)
tree.heading('#10', text="CantMB", anchor=CENTER)
tree.column('#11',width=40)
tree.heading('#11', text="CantPreservantes", anchor=CENTER)
tree.column('#12',width=40)
tree.heading('#12', text="CantContraMuestra", anchor=CENTER)
tree.column('#13',width=40)
tree.heading('#13', text="FechaMuestra", anchor=CENTER)


def seleccionarUsandoClick(event):
	item=tree.identify('item',event.x,event.y)
	miId.set(tree.item(item,"text"))
	miSolicitud.set(tree.item(item,"values")[0])
	miAviso.set(tree.item(item,"values")[1])
	miFormula.set(tree.item(item,"values")[2])

tree.bind("<Double-1>", seleccionarUsandoClick)



def actualizar():
	miConexion=sqlite3.connect("base.db")
	miCursor=miConexion.cursor()
	try:
		datos=miSolicitud.get(),miAviso.get(),miFormula.get(),miDescripcion.get(),miFechaIngreso.get(),miTipo.get(),miTiempo.get(),miTemperatura.get(),miCantFQ.get(),miCantPreservantes.get(),miCantContraMuestra.get(),miFechaMuestra.get()
		miCursor.execute("UPDATE tblDatos SET Solicitud=?, Aviso=?, Formula=? WHERE ID="+miId.get(), (datos))
		miConexion.commit()
	except:
		messagebox.showwarning("ADVERTENCIA","Ocurrió un error al actualizar el registro")
		pass
	limpiarCampos()
	mostrar()

def borrar():
	miConexion=sqlite3.connect("base.db")
	miCursor=miConexion.cursor()
	try:
		if messagebox.askyesno(message="¿Realmente desea eliminar el registro?", title="ADVERTENCIA"):
			miCursor.execute("DELETE FROM tblDatos WHERE ID="+miId.get())
			miConexion.commit()
	except:
		messagebox.showwarning("ADVERTENCIA","Ocurrió un error al tratar de eliminar el registro")
		print(miId)
		pass
	limpiarCampos()
	mostrar()

###################### Colocar widgets en la VISTA ######################
########## Creando Los menus ###############
menubar=Menu(root)
menubasedat=Menu(menubar,tearoff=0)
menubasedat.add_command(label="Crear/Conectar Base de Datos", command=conexionBBDD)
menubasedat.add_command(label="Eliminar Base de Datos", command=eliminarBBDD)
menubasedat.add_command(label="Salir", command=salirAplicacion)
menubar.add_cascade(label="Inicio", menu=menubasedat)

ayudamenu=Menu(menubar,tearoff=0)
ayudamenu.add_command(label="Resetear Campos", command=limpiarCampos)
ayudamenu.add_command(label="Acerca", command=mensaje)
menubar.add_cascade(label="Ayuda",menu=ayudamenu)

############## Creando etiquetas y cajas de texto ###########################
#e1=Entry(root, textvariable=miId, width=50)
#e1.place(x=1, y=1)

l2=Label(root, text="Solicitud")
l2.place(x=20,y=10)
e2=Entry(root, textvariable=miSolicitud, width=50)
e2.place(x=150, y=10)

l3=Label(root, text="Aviso")
l3.place(x=20,y=30)
e3=Entry(root, textvariable=miAviso, width=50)
e3.place(x=150, y=30)

l4=Label(root, text="Formula")
l4.place(x=20,y=50)
e4=Entry(root, textvariable=miFormula, width=50)
e4.place(x=150, y=50)

l5=Label(root, text="Descripcion")
l5.place(x=20,y=70)
e5=Entry(root, textvariable=miDescripcion, width=50)
e5.place(x=150, y=70)

l6=Label(root, text="FechaIngreso")
l6.place(x=20,y=90)
e6=DateEntry(root, textvariable=miFechaIngreso)
e6.place(x=150, y=90)

l7=Label(root, text="Tipo")
l7.place(x=20,y=110)
#e7=Entry(root, textvariable=miTipo, width=50)
e7=ttk.Combobox(root, textvariable=miTipo,
                            values=[
                                    "Natural", 
                                    "Acelerada",
                                    "Compatibilidad",
                                    "Diseño"],
									state="readonly")
e7.place(x=150, y=110)

l8=Label(root, text="Tiempo")
l8.place(x=20,y=130)
#e8=Entry(root, textvariable=miTiempo, width=50)
e8=ttk.Combobox(root, textvariable=miTiempo,
                            values=[
                                    "0", 
                                    "15",
                                    "30",
									"60",
									"90",
									"180",
									"270",
									"540",
									"720",
									"900",
									"1080"],
									state="readonly")
e8.place(x=150, y=130)

l9=Label(root, text="Temperatura")
l9.place(x=20,y=150)
#e9=Entry(root, textvariable=miTemperatura, width=50)
e9=ttk.Combobox(root, textvariable=miTemperatura,
                            values=[
                                    "0", 
                                    "4",
                                    "40",
									"50"],
									state="readonly")
e9.place(x=150, y=150)

l10=Label(root, text="CantFQ")
l10.place(x=20,y=170)
e10=Entry(root, textvariable=miCantFQ, width=50)
e10.place(x=150, y=170)

l10=Label(root, text="CantMB")
l10.place(x=20,y=190)
e10=Entry(root, textvariable=miCantMB, width=50)
e10.place(x=150, y=190)

l11=Label(root, text="CantPreservantes")
l11.place(x=20,y=210)
e11=Entry(root, textvariable=miCantPreservantes, width=50)
e11.place(x=150, y=210)

l12=Label(root, text="CantContraMuetra")
l12.place(x=20,y=230)
e12=Entry(root, textvariable=miCantContraMuestra, width=50)
e12.place(x=150, y=230)

dta = (str(miFechaIngreso.get()))
dtt = (int(miTiempo.get()))
print(dta)

dt = datetime.datetime.strptime(dta, '%d/%m/%y') + datetime.timedelta(days=dtt)

miFechaMuestra = (str(dt))

l13=Label(root, text="FechaMuestra")
l13.place(x=20,y=250)
e13=Entry(root, textvariable=miFechaMuestra)
e13.place(x=150, y=250)

################# Creando botones ###########################

b1=Button(root, text="Crear Registro", command=crear)
b1.place(x=650, y=10)
b2=Button(root, text="Modificar Registro", command=actualizar)
b2.place(x=650, y=40)
b3=Button(root, text="Mostrar Lista", command=mostrar)
b3.place(x=650, y=70)
b4=Button(root, text="Eliminar Registro",bg="red", command=borrar)
b4.place(x=650, y=100)


root.config(menu=menubar)


root.mainloop()
