import tkinter as tk
from tkinter import filedialog

def mostrar_resultado():
    seleccion = variable.get()
    cuadro_texto.delete(1.0, tk.END) 
    cuadro_texto.insert(tk.END, f"La opción elegida es: {seleccion}")

def mostrar_contenido_archivo():
    ruta_archivo = variable.get()
    if ruta_archivo != "Opciones":
        try:
            with open(ruta_archivo, "r") as archivo:
                contenido = archivo.read()
                cuadro_texto.delete(1.0, tk.END)
                cuadro_texto.insert(tk.END, contenido)
                aplicar_estilos(contenido)
        except Exception as e:
            cuadro_texto.delete(1.0, tk.END)
            cuadro_texto.insert(tk.END, f"Error al abrir el archivo: {str(e)}")

def aplicar_estilos(texto):
    cuadro_texto.tag_configure("negrita", font=("Arial", 12, "bold"))
    cuadro_texto.tag_configure("negrita", font=("Arial", 12, "bold"))
    cuadro_texto.tag_configure("negrita", font=("Arial", 12, "bold"))

    inicio = 1.0
    final = "end"

    cuadro_texto.tag_add("normal", inicio, final)

    cuadro_texto.tag_add("cursiva", inicio + 30, inicio + 40)

def subir():
    cuadro_texto.yview_scroll(-1, "units")

def bajar():
    cuadro_texto.yview_scroll(1, "units")

ventana = tk.Tk()
ventana.title("Menú de archivos .log")

titulo_etiqueta = tk.Label(ventana, text="Seleccione una opción de archivos de access.log", font=("Arial", 14, "italic", "underline"))
titulo_etiqueta.pack(pady=10)

etiqueta_opciones = tk.Label(ventana, text="Opciones a elegir:", font=("Arial", 14, "italic"))
etiqueta_opciones.pack(pady=10)

opciones = ["Opciones", "C:\\xampp\\apache\\logs\\access.log",
            "C:\\xampp\\apache\\logs\\error.log",
            "C:\\xampp\\apache\\logs\\install.log",
            "C:\\xampp\\apache\\logs\\ssl_request.log"]

variable = tk.StringVar(ventana)
variable.set(opciones[0])  

menu_desplegable = tk.OptionMenu(ventana, variable, *opciones)
menu_desplegable.pack(pady=10)

variable.trace_add("write", lambda *args: mostrar_resultado())

boton_mostrar_contenido = tk.Button(ventana, text="Mostrar Contenido", command=mostrar_contenido_archivo, bg="violet", fg="white")
boton_mostrar_contenido.pack(pady=10)

cuadro_texto = tk.Text(ventana, height=25, width=100)
cuadro_texto.pack(pady=10)

boton_subir = tk.Button(ventana, text="Subir", command=subir)
boton_subir.pack(side="left", padx=10)
boton_bajar = tk.Button(ventana, text="Bajar", command=bajar)
boton_bajar.pack(side="left", padx=10)

ventana.mainloop()
