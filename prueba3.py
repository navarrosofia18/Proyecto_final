import tkinter as tk
from tkinter import filedialog
import configparser

# Configuración por defecto
config = configparser.ConfigParser()
config.read_dict({
    'Settings': {'theme': 'light'},
    'light': {
        'ventana_bg': '#1E1E1E',
        'titulo_etiqueta_bg': 'white',
        'titulo_etiqueta_fg': '#1E1E1E',
        'etiqueta_opciones_bg': '#1E1E1E',
        'etiqueta_opciones_fg': 'white',
        'boton_mostrar_contenido_bg': 'purple',
        'boton_mostrar_contenido_fg': 'white',
        'cuadro_texto_bg': '#1E1E1E',
        'cuadro_texto_fg': 'white',
        'cuadro_texto_insertbackground': 'white',
        'boton_subir_bg': '#333',
        'boton_subir_fg': 'white',
        'boton_bajar_bg': '#333',
        'boton_bajar_fg': 'white'
    },
    'dark': {
        'ventana_bg': 'white',
        'titulo_etiqueta_bg': 'white',
        'titulo_etiqueta_fg': 'black',
        'etiqueta_opciones_bg': 'white',
        'etiqueta_opciones_fg': 'black',
        'boton_mostrar_contenido_bg': 'violet',
        'boton_mostrar_contenido_fg': 'white',
        'cuadro_texto_bg': 'white',
        'cuadro_texto_fg': 'black',
        'cuadro_texto_insertbackground': 'black',
        'boton_subir_bg': '#DDD',
        'boton_subir_fg': 'black',
        'boton_bajar_bg': '#DDD',
        'boton_bajar_fg': 'black'
    }
})

# Crear la instancia de Tk antes de realizar configuraciones
ventana = tk.Tk()
ventana.title("Menú de archivos .log")
ventana.geometry("800x500")

# Defino las variables globales que traigo del .ini
ventana_bg = ""
titulo_etiqueta_fg = ""
titulo_etiqueta_bg = ""
etiqueta_opciones_bg = ""
etiqueta_opciones_fg = ""
boton_mostrar_contenido_bg = ""
boton_mostrar_contenido_fg = ""
cuadro_texto_bg = ""
cuadro_texto_fg = ""
cuadro_texto_insertbackground = ""
boton_subir_bg = ""
boton_subir_fg = ""
boton_bajar_bg = ""
boton_bajar_fg = ""

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
    cuadro_texto.tag_configure("normal", font=("Arial", 12))
    cuadro_texto.tag_configure("cursiva", font=("Arial", 12, "italic"))
    cuadro_texto.tag_configure("negrita", font=("Arial", 12, "bold"))

    inicio = 1.0
    final = "end"

    cuadro_texto.tag_add("normal", inicio, final)

    # Estilo a las letras 
    cuadro_texto.tag_add("cursiva", inicio + 30, inicio + 40)

def subir():
    cuadro_texto.yview_scroll(-1, "units")

def bajar():
    cuadro_texto.yview_scroll(1, "units")

titulo_etiqueta = tk.Label(ventana, text="Seleccione una opción de archivos de access.log", font=("Arial", 14, "italic", "underline"))
etiqueta_opciones = tk.Label(ventana, text="Opciones a elegir:", font=("Arial", 14, "italic"))
boton_mostrar_contenido = tk.Button(ventana, text="Mostrar Contenido", command=mostrar_contenido_archivo)
cuadro_texto = tk.Text(ventana, height=25, width=100)
boton_subir = tk.Button(ventana, text="Subir", command=subir)
boton_bajar = tk.Button(ventana, text="Bajar", command=bajar)

def guardar_configuracion():
    config.set('Settings', 'theme', tema_actual)
    with open('config.ini', 'w') as configfile:
        config.write(configfile)

def cargar_configuracion():
    global tema_actual
    try:
        tema_actual = config.get('Settings', 'theme')
        cambiar_tema(tema_actual)
    except configparser.Error:
        print("Error al leer el archivo de configuración. Se utilizará el tema por defecto.")

def cambiar_tema(tema):
    global tema_actual
    tema_actual = tema

    if tema == "dark":
        aplicar_estilos_tema(config['dark'])
    else:  # Tema claro
        aplicar_estilos_tema(config['light'])

def aplicar_estilos_tema(estilos):
    global cuadro_texto_bg, cuadro_texto_fg, cuadro_texto_insertbackground
    cuadro_texto_bg = estilos['cuadro_texto_bg']
    cuadro_texto_fg = estilos['cuadro_texto_fg']
    cuadro_texto_insertbackground = estilos['cuadro_texto_insertbackground']

    ventana.config(bg=estilos['ventana_bg'])
    titulo_etiqueta.config(bg=estilos['titulo_etiqueta_bg'], fg=estilos['titulo_etiqueta_fg'])
    etiqueta_opciones.config(bg=estilos['etiqueta_opciones_bg'], fg=estilos['etiqueta_opciones_fg'])
    boton_mostrar_contenido.config(bg=estilos['boton_mostrar_contenido_bg'], fg=estilos['boton_mostrar_contenido_fg'])
    cuadro_texto.config(bg=cuadro_texto_bg, fg=cuadro_texto_fg, insertbackground=cuadro_texto_insertbackground)
    boton_subir.config(bg=estilos['boton_subir_bg'], fg=estilos['boton_subir_fg'])
    boton_bajar.config(bg=estilos['boton_bajar_bg'], fg=estilos['boton_bajar_fg'])

def mostrar_resultado():
    seleccion = variable.get()
    cuadro_texto.delete(1.0, tk.END) 
    cuadro_texto.insert(tk.END, f"La opción elegida es: {seleccion}")

# Cargar configuración
cargar_configuracion()

titulo_etiqueta.pack(pady=10)
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

boton_mostrar_contenido.pack(pady=10)
cuadro_texto.pack(pady=10)
boton_subir.pack(side="left", padx=10)
boton_bajar.pack(side="left", padx=10)

boton_tema_oscuro = tk.Button(ventana, text="Tema Oscuro", command=lambda: cambiar_tema("light"))
boton_tema_oscuro.pack(side="right", padx=10)
boton_tema_claro = tk.Button(ventana, text="Tema Claro", command=lambda: cambiar_tema("dark"))
boton_tema_claro.pack(side="right", padx=10)

ventana.mainloop()
