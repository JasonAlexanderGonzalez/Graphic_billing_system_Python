import tkinter as tk
import tkinter as ttk
import tkinter.messagebox as messagebox
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tkinter import ttk
from tkinter import scrolledtext
from tkinter import Menu
from tkinter import messagebox as mBox
import mysql.connector


def guardar_informacion(id_value, descripcion_value, precio_value, cantidad_value):

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
    mBox.showinfo("Información guardada",
                  "La información ha sido guardada exitosamente  en la base de datos")


def funcion_add():
    ventana_add = tk.Toplevel(ventana)
    ventana_add.title("Agregar Informacion ")
    ventana_add.geometry("600x300")
    ventana_add.resizable(0, 0)  # denied resizable

    id_label = tk.Label(ventana_add, text=" ID: ").grid(row=0, column=0)
    id_entry = tk.Entry(ventana_add, width=70)
    id_entry.grid(row=0, column=1)

    descripcion_label = tk.Label(
        ventana_add, text=" Descripcion: ").grid(row=1, column=0)
    descripcion_entry = tk.Entry(ventana_add, width=70)
    descripcion_entry.grid(row=1, column=1)

    precio_label = tk.Label(ventana_add, text="Precio").grid(row=2, column=0)
    precio_entry = tk.Entry(ventana_add, width=70)
    precio_entry.grid(row=2, column=1)

    cantidad_label = tk.Label(
        ventana_add, text="Cantidad").grid(row=3, column=0)
    cantidad_entry = tk.Entry(ventana_add, width=70)
    cantidad_entry.grid(row=3, column=1)

    # Agrega un botón "Guardar" que llama a la función guardar_informacion() con los valores ingresados
    guardar_button = tk.Button(ventana_add, text="Guardar", command=lambda: guardar_informacion(
        id_entry.get(), descripcion_entry.get(), precio_entry.get(), cantidad_entry.get()))
    guardar_button.grid(row=4, column=0, columnspan=2)


def eliminar_registro(id_eliminar, label_resultado):

    # Conectar a la base de datos
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="12345",
        database="pybd"
    )
    # Crear un cursor para hacer consultas
    mycursor = mydb.cursor()
    # Eliminar el registro de la tabla productos
    mycursor.execute("DELETE FROM productos WHERE id = %s", (id_eliminar,))
    mydb.commit()
    # Obtener el número de registros eliminados
    num_registros_eliminados = mycursor.rowcount

    # Mostrar el resultado en la etiqueta correspondiente
    if num_registros_eliminados > 0:
        label_resultado.config(
            text=f"Se eliminó el registro con ID {id_eliminar}.")
        messagebox.showinfo(
            title="Mensaje", message="Se eliminó el registro: ")
    else:
        label_resultado.config(
            text="No se encontró ningún registro con ese ID.")
        messagebox.showinfo(
            title="Mensaje", message="No se encontró ningún registro con ese ID")


def funcion_delete():
    ventana_delete = tk.Toplevel(ventana)
    ventana_delete.title("Eliminar Informacion")
    ventana_delete.geometry("300x200")
    ventana_delete.resizable(0, 0)

    # Crear una etiqueta para pedirle al usuario que ingrese un ID a eliminar
    label_eliminar = tk.Label(ventana_delete, text="Ingrese el ID a eliminar:")
    label_eliminar.pack()

    # Crear un Entry widget para que el usuario ingrese el ID a eliminar
    entry_eliminar = tk.Entry(ventana_delete)
    entry_eliminar.pack()

    # Crear un botón para eliminar el registro
    boton_eliminar = tk.Button(ventana_delete, text="Eliminar", command=lambda: eliminar_registro(
        entry_eliminar.get(), label_resultado))
    boton_eliminar.pack()

    # Crear una etiqueta para mostrar el resultado de la eliminación
    label_resultado = tk.Label(ventana_delete)
    label_resultado.pack()


def funcion_update():
    ventana_update = tk.Toplevel(ventana)
    ventana_update.title("Agregar Informacion ")
    update.geometry("300x200")


def funcion_exit():
    ventana.quit()
    ventana.destroy()
    exit


def funcion_estadisticas():
    # Conectar a la base de datos
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="12345",
        database="pybd"
    )
    # Crear un cursor para hacer consultas
    mycursor = mydb.cursor()
    # Hacer la consulta a la tabla productos
    mycursor.execute(
        "SELECT COUNT(*), MIN(precio), MAX(precio), AVG(precio) FROM productos")
    resultado = mycursor.fetchone()

    if resultado:
        # Crear una ventana para mostrar la tabla con las estadísticas
        ventana_estadisticas = tk.Toplevel(ventana)
        ventana_estadisticas.title("Estadísticas")
        ventana_estadisticas.geometry("800x300")
       # ventana_estadisticas.resizable(0,0)

        # Crear una tabla usando el widget Treeview de ttk
        tabla_estadisticas = ttk.Treeview(
            ventana_estadisticas, columns=("count", "min", "max", "avg"))
        tabla_estadisticas.heading("#0", text="Estadística")
        tabla_estadisticas.heading("count", text="Cantidad de Productos")
        tabla_estadisticas.heading("min", text="Precio Mínimo")
        tabla_estadisticas.heading("max", text="Precio Máximo")
        tabla_estadisticas.heading("avg", text="Precio Promedio")

        # Insertar los datos de las estadísticas en la tabla
        tabla_estadisticas.insert("", "end", text="Productos", values=(
            resultado[0], resultado[1], resultado[2], resultado[3]))

        # Mostrar la tabla en la ventana
        tabla_estadisticas.pack()

    else:
        messagebox.showerror(
            "Error", "No se encontraron productos en la base de datos.")


def funcion_read_all():
    ventana_read_all = tk.Toplevel(ventana)
    ventana_read_all.title("Toda la informacion")
    ventana_read_all.geometry("600x300")
    ventana_read_all.resizable(0, 0)

    # Crear un Treeview para mostrar los datos
    treeview = ttk.Treeview(ventana_read_all)
    treeview.pack(fill='both', expand=True)

    # Agregar las columnas al Treeview
    treeview['columns'] = ('ID', 'Descripcion', 'Precio')
    treeview.column('#0', width=0, stretch='no')
    treeview.column('ID', anchor='center', width=100)
    treeview.column('Descripcion', anchor='w', width=300)
    treeview.column('Precio', anchor='center', width=100)

    # Agregar los encabezados de las columnas
    treeview.heading('#0', text='', anchor='center')
    treeview.heading('ID', text='ID', anchor='center')
    treeview.heading('Descripcion', text='Descripcion', anchor='w')
    treeview.heading('Precio', text='Precio', anchor='center')

    # Conectar a la base de datos
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="12345",
        database="pybd"
    )

    # Crear un cursor para hacer consultas
    mycursor = mydb.cursor()

    # Hacer la consulta a la tabla productos
    mycursor.execute("SELECT * FROM productos")
    resultados = mycursor.fetchall()

    # Agregar los datos al Treeview
    for resultado in resultados:
        treeview.insert(parent='', index='end', values=resultado)

    # Ajustar el ancho de las columnas al contenido
    for column in treeview['columns']:
        treeview.column(column, width=tk.FORCE)


# def funcion_read_all():
 #   ventana_read_all = tk.Toplevel(ventana)
  #  ventana_read_all.title("Toda la informacion")
   # ventana_read_all.geometry("600x300")
    # ventana_read_all.resizable(0,0)

    # Conectar a la base de datos
    # mydb = mysql.connector.connect(
     #   host="localhost",
      #  user="root",
       # password="12345",
        # database="pybd"
   # )
    # Crear un cursor para hacer consultas
   # mycursor = mydb.cursor()
    # Hacer la consulta a la tabla productos
   # mycursor.execute("SELECT * FROM productos")
    # resultados = mycursor.fetchall()

    # Crear un Text widget para mostrar los resultados
    # text_resultados = tk.Text(ventana_read_all)
    # text_resultados.pack()

    # Agregar los resultados al Text widget
    for resultado in resultados:
        text_resultados.insert(
            tk.END, f"id: {resultado[0]}, descripcion: {resultado[1]}, precio: {resultado[2]}\n")


def funcion_read():
    ventana_read = tk.Toplevel(ventana)
    ventana_read.title("Buscar Informacion")
    ventana_read.geometry("600x300")
    ventana_read.resizable(0, 0)

    # Crear una etiqueta para pedirle al usuario que ingrese un término de búsqueda
    label_buscar = tk.Label(ventana_read, text="Ingrese el id a consultar:")
    label_buscar.pack()

    # Crear un Entry widget para que el usuario ingrese el término de búsqueda
    entry_buscar = tk.Entry(ventana_read)
    entry_buscar.pack()

    # Crear un botón para realizar la búsqueda
    boton_buscar = tk.Button(ventana_read, text="Buscar", command=lambda: buscar_info(
        entry_buscar.get(), label_resultado))
    boton_buscar.pack()

    # Crear una etiqueta para mostrar el resultado de la búsqueda
    label_resultado = tk.Label(ventana_read)
    label_resultado.pack()


def buscar_info(id_busqueda, label_resultado):
    # Buscar en la base de datos pybd
    encontrado_pybd = False
    # Conectar a la base de datos
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="12345",
        database="pybd"
    )
    # Crear un cursor para hacer consultas
    mycursor = mydb.cursor()
    # Hacer la consulta a la tabla productos
    mycursor.execute("SELECT * FROM productos WHERE id = %s", (id_busqueda,))
    resultado = mycursor.fetchone()
    if resultado:
        encontrado_pybd = True
        resultado = f"id: {resultado[0]}, descripcion: {resultado[1]}, precio: {resultado[2]}"
    # Mostrar el resultado en la etiqueta correspondiente
    if encontrado_pybd:
        label_resultado.config(
            text=f"La información fue encontrada en la base de datos: {resultado}")
    else:
        label_resultado.config(text="La información no fue encontrada.")


ventana = tk.Tk()
ventana.title('System')
ventana.geometry("800x800")  # size of the board
ventana.resizable(0, 0)  # denied resizable

barra_menu = Menu(ventana)
ventana.config(menu=barra_menu)

canvas = tk.Canvas(ventana, width=800, height=800)
canvas.pack(fill=tk.BOTH, expand=True)
image = tk.PhotoImage(file="python.png")
canvas.create_image(0, 0, image=image, anchor=tk.NW)

menu_ayuda = Menu(barra_menu, tearoff=0)
menu_ayuda.add_command(label=" Add ", command=funcion_add)
menu_ayuda.add_separator()
menu_ayuda.add_command(label=" Delete ", command=funcion_delete)
menu_ayuda.add_separator()
menu_ayuda.add_command(label=" Update ", command=funcion_update)
menu_ayuda.add_separator()
menu_ayuda.add_command(label=" Read ", command=funcion_read)
menu_ayuda.add_separator()
menu_ayuda.add_command(label=" Read All", command=funcion_read_all)
menu_ayuda.add_separator()
menu_ayuda.add_command(label=" Statics", command=funcion_estadisticas)
menu_ayuda.add_separator()
barra_menu.add_cascade(label="Products", menu=menu_ayuda)

final_menu = Menu(barra_menu)
barra_menu.add_cascade(label=" About ", menu=final_menu)

exit_menu = Menu(barra_menu)
exit_menu.add_command(label=" Exit.. ", command=funcion_exit)
menu_ayuda.add_separator()
barra_menu.add_cascade(label="Exit", menu=exit_menu)


ventana.mainloop()
