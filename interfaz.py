import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext
from tkinter import Menu
from tkinter import messagebox as mBox
import mysql.connector


#def guardar_informacion(id_value, descripcion_value, precio_value, cantidad_value):
    # Almacena los valores ingresados en una lista
   # informacion = [id_value, descripcion_value, precio_value, cantidad_value]
    
    # Abre el archivo "agregar.txt" en modo de escritura
  #  with open("agregar.txt", "a") as archivo:
        # Escribe la información en una línea separada por comas
      #  archivo.write(",".join(informacion) + "\n")
        
        # Muestra un mensaje de confirmación
      #  mBox.showinfo("Información guardada", "La información ha sido guardada exitosamente en el archivo 'agregar.txt'")
        
def guardar_informacion(id_value, descripcion_value, precio_value, cantidad_value):
    # Almacena los valores ingresados en una lista
    informacion = [id_value, descripcion_value, precio_value, cantidad_value]
    
    # Abre el archivo "agregar.txt" en modo de escritura
    with open("agregar.txt", "a") as archivo:
        # Escribe la información en una línea separada por comas
        archivo.write(",".join(informacion) + "\n")
        
        # Conecta a la base de datos
        mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="12345",
    database="pybd"
)

        
        # Prepara la consulta SQL
        mycursor = mydb.cursor()
        sql = "INSERT INTO productos (id, descripcion, precio, cantidad) VALUES (%s, %s, %s, %s)"
        val = (id_value, descripcion_value, precio_value, cantidad_value)

        # Ejecuta la consulta SQL y guarda los cambios en la base de datos
        mycursor.execute(sql, val)
        mydb.commit()
        
        # Muestra un mensaje de confirmación
        mBox.showinfo("Información guardada", "La información ha sido guardada exitosamente en el archivo 'agregar.txt' y en la base de datos")
        
def funcion_add():
    ventana_add = tk.Toplevel(ventana)
    ventana_add.title("Agregar Informacion ")
    ventana_add.geometry("600x300")   
    ventana_add.resizable(0,0)  #denied resizable
    
    id_label = tk.Label(ventana_add, text=" ID: ").grid(row=0, column=0)
    id_entry = tk.Entry(ventana_add, width=70)
    id_entry.grid(row=0, column=1)
    
 
    descripcion_label = tk.Label(ventana_add, text=" Descripcion: ").grid(row=1, column=0)
    descripcion_entry = tk.Entry(ventana_add, width=70)
    descripcion_entry.grid(row=1, column=1)
    
    precio_label = tk.Label(ventana_add, text="Precio").grid(row=2, column=0)
    precio_entry = tk.Entry(ventana_add, width=70)
    precio_entry.grid(row=2, column=1)
    
    cantidad_label = tk.Label(ventana_add, text="Cantidad").grid(row=3, column=0)
    cantidad_entry = tk.Entry(ventana_add, width=70)
    cantidad_entry.grid(row=3, column=1)
    
    # Agrega un botón "Guardar" que llama a la función guardar_informacion() con los valores ingresados
    guardar_button = tk.Button(ventana_add, text="Guardar", command=lambda: guardar_informacion(id_entry.get(), descripcion_entry.get(), precio_entry.get(), cantidad_entry.get()))
    guardar_button.grid(row=4, column=0, columnspan=2)


def funcion_delete():
    ventana_delete = tk.Toplevel(ventana)
    ventana_delete.title("Eliminar Informacion ")
    ventana_delete.geometry("300x200")
    
   
    
def funcion_update():
    ventana_update = tk.Toplevel(ventana)
    ventana_update.title("Agregar Informacion ")
    update.geometry("300x200")    


def funcion_exit():
    ventana.quit()
    ventana.destroy()
    exit
    

def funcion_read():
    ventana_read = tk.Toplevel(ventana)
    ventana_read.title("Buscar Informacion ")
    ventana_read.geometry("300x200")
    

ventana = tk.Tk()
ventana.title('System')
ventana.geometry("800x800") #size of the board
ventana.resizable(0,0)  #denied resizable

barra_menu = Menu(ventana)
ventana.config(menu=barra_menu)

canvas = tk.Canvas(ventana, width=800, height=800)
canvas.pack(fill=tk.BOTH, expand=True)
image = tk.PhotoImage(file="python.png")
canvas.create_image(0,0, image=image, anchor=tk.NW)

menu_ayuda = Menu(barra_menu, tearoff=0)
menu_ayuda.add_command(label=" Add ", command=funcion_add)
menu_ayuda.add_separator()
menu_ayuda.add_command(label=" Delete ", command=funcion_delete)
menu_ayuda.add_separator()
menu_ayuda.add_command(label=" Update ", command=funcion_update)
menu_ayuda.add_separator()
menu_ayuda.add_command(label=" Read ", command=funcion_read)
menu_ayuda.add_separator()
barra_menu.add_cascade(label="Products", menu=menu_ayuda)

final_menu = Menu(barra_menu)
barra_menu.add_cascade(label=" About ", menu=final_menu)

exit_menu = Menu(barra_menu)
exit_menu.add_command(label=" Exit.. ", command=funcion_exit)
menu_ayuda.add_separator()
barra_menu.add_cascade(label = "Exit", menu =exit_menu )


ventana.mainloop()