from tkinter import *
from tkinter import messagebox
import sqlite3

#-------------Funcion-----------
def conexion_BBDD():
    conexion=sqlite3.connect("Usuarios")
    cursor=conexion.cursor()
    try:
        cursor.execute('''
            CREATE TABLE Datos_usuarios(
                ID integer primary key autoingrement,
                Nombre text,
                Contraseña text,
                Apellido text,
                Comentario text)
                ''')
        messagebox.showinfo("BBDD", "Base de datos creada con exito")
    except:
        messagebox.showwarning("Atencion","La base de datos ya existe")

def cerrar_aplicacion():
        valor=messagebox.askquestion("Salir", "¿Deseas Salir de la aplicacion?")
            
        if valor=="yes":
                
            root.destroy()
            
            
def limpiar_campos():
    mi_id.set("")
    mi_nombre.set("")
    mi_password.set("")
    mi_apellido.set("")
    input_comentario.delete(1.0, END)
    
def crear_post():
    conexion=sqlite3.conect("Usuarios")
    cursor=conexion.cursor()
    cursor.execute("INSERT INTO Datos_usuarios VALUES(NULL, '"+ input_nombre.get "','") + ")
        
        
root=Tk()
root.title("CRUD con PYTHON")


barra_menu=Menu(root)
root.config(menu=barra_menu, width=300, height=300,background="Salmon")

bbdd_menu=Menu(barra_menu, tearoff=0)
bbdd_menu.add_command(label="Conectar", command=conexion_BBDD)
bbdd_menu.add_command(label="Salir", command=cerrar_aplicacion)

borrar_menu=Menu(barra_menu, tearoff=0)
borrar_menu.add_command(label="Borrar campos",command=limpiar_campos)

CRUD_menu=Menu(barra_menu, tearoff=0)
CRUD_menu.add_command(label="Crear")
CRUD_menu.add_command(label="Leer")
CRUD_menu.add_command(label="Actualizar")
CRUD_menu.add_command(label="Borrar")

ayuda_menu=Menu(barra_menu, tearoff=0)
ayuda_menu.add_command(label="Acerca de...")
ayuda_menu.add_command(label="Licencia")

barra_menu.add_cascade(label="BBDD", menu=bbdd_menu)
barra_menu.add_cascade(label="Borrar", menu=borrar_menu)
barra_menu.add_cascade(label="CRUD", menu=CRUD_menu)
barra_menu.add_cascade(label="Ayuda", menu=ayuda_menu)

#------aqui van los input esto es organizado en un regilla
primer_frame=Frame(root)
primer_frame.config(background="lightSkyBlue")
primer_frame.pack()

mi_id=StringVar()
mi_nombre=StringVar()
mi_password=StringVar()
mi_apellido=StringVar()

input_id=Entry(primer_frame, textvariable=mi_id)
input_id.grid(row=0, column=1, padx=10,pady=10)
input_id.config(fg="red", justify="right")

input_nombre=Entry(primer_frame, textvariable=mi_nombre)
input_nombre.grid(row=1, column=1, padx=10,pady=10)

input_password=Entry(primer_frame, textvariable=mi_password)
input_password.grid(row=2, column=1, padx=10,pady=10)
input_password.config(show="*")

input_apellido=Entry(primer_frame, textvariable=mi_apellido)
input_apellido.grid(row=3, column=1, padx=10,pady=10)

input_comentario=Text(primer_frame, width=16, height=5)
input_comentario.grid(row=4, column=1,pady=10)
scrollVert=Scrollbar(primer_frame, command=input_comentario.yview)
scrollVert.grid(row=4, column=2, sticky="nsew",pady=10)


input_comentario.config(yscrollcommand=scrollVert.set)

#-----vamos a introducir los textos acompañados a los inputs

label_id=Label(primer_frame, text="Id:")
label_id.grid(row=0,column=0, sticky="e",padx=10, pady=10)
label_id.config(background="lightSkyBlue")

label_nombre=Label(primer_frame, text="Nombre:")
label_nombre.grid(row=1,column=0, sticky="e",padx=10, pady=10)
label_nombre.config(background="lightSkyBlue")

label_password=Label(primer_frame, text="Password:")
label_password.grid(row=2,column=0, sticky="e",padx=10, pady=10)
label_password.config(background="lightSkyBlue")

label_apellido=Label(primer_frame, text="Apellido:")
label_apellido.grid(row=3,column=0, sticky="e",padx=10, pady=10)
label_apellido.config(background="lightSkyBlue")

label_comentario=Label(primer_frame, text="Comentario:")
label_comentario.grid(row=4,column=0, sticky="e",padx=10, pady=10)
label_comentario.config(background="lightSkyBlue")


##Segundo frame para poner los botones

segundo_frame=Frame(root)
segundo_frame.config(background="lightSkyBlue")
segundo_frame.pack()

boton_crear=Button(segundo_frame, text="Crear")
boton_crear.grid(row=1, column=0, sticky="e", padx=10, pady=10)

boton_leer=Button(segundo_frame, text="Leer")
boton_leer.grid(row=1, column=1, sticky="e", padx=10, pady=10)

boton_update=Button(segundo_frame, text="Actualizar")
boton_update.grid(row=1, column=2, sticky="e", padx=10, pady=10)

boton_borrar=Button(segundo_frame, text="Borrar")
boton_borrar.grid(row=1, column=3, sticky="e", padx=10, pady=10)











root.mainloop()


