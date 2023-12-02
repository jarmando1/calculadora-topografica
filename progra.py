import tkinter as tk
from PIL import Image, ImageTk
import math

def calcular_distancia(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def calcular_area(coordenadas):
    n = len(coordenadas)
    area = 0
    for i in range(n):
        x1, y1 = coordenadas[i]
        x2, y2 = coordenadas[(i + 1) % n]
        area += (x1 * y2) - (x2 * y1)
    return abs(area) / 2

def agregar_coordenada():
    x = float(entry_x.get())
    y = float(entry_y.get())
    coordenadas.append((x, y))
    entry_x.delete(0, tk.END)
    entry_y.delete(0, tk.END)
    actualizar_lista_coordenadas()
    boton_eliminar.config(state=tk.NORMAL)  # Reactivar el botón después de agregar coordenada

def eliminar_coordenada():
    seleccion = lista_coordenadas.curselection()
    if seleccion:
        index = int(seleccion[0])
        del coordenadas[index]
        actualizar_lista_coordenadas()

def actualizar_lista_coordenadas():
    lista_coordenadas.delete(0, tk.END)
    for coord in coordenadas:
        lista_coordenadas.insert(tk.END, f"({coord[0]}, {coord[1]})")

def calcular_resultado():
    if len(coordenadas) < 3:
        resultado.set("Se requieren al menos 3 coordenadas para calcular el área y distancia.")
        return
    distancia_total = 0
    for i in range(len(coordenadas)):
        x1, y1 = coordenadas[i]
        x2, y2 = coordenadas[(i + 1) % len(coordenadas)]
        distancia = calcular_distancia(x1, y1, x2, y2)
        distancia_total += distancia
    area = calcular_area(coordenadas)
    resultado_text = f"Distancia total: {distancia_total:.2f} unidades\nÁrea del polígono: {area:.2f} unidades cuadradas"
    resultado.set(resultado_text)

    # Guardar la distancia y el área en un archivo de texto
    with open("resultado.txt", "w") as file:
        file.write(f"Distancia total: {distancia_total:.2f} unidades\nÁrea del polígono: {area:.2f} unidades cuadradas")

def salir():
    ventana.destroy()

ventana = tk.Tk()
ventana.title("Calculadora Topográfica")

# Declarar resultado como una variable global
resultado = tk.StringVar()

coordenadas = []

frame_entrada = tk.Frame(ventana)
frame_resultado = tk.Frame(ventana)

frame_entrada.pack(padx=10, pady=10)
frame_resultado.pack(padx=10, pady=10)

label_x = tk.Label(frame_entrada, text="Coordenada X:")
label_y = tk.Label(frame_entrada, text="Coordenada Y:")
entry_x = tk.Entry(frame_entrada)
entry_y = tk.Entry(frame_entrada)
boton_agregar = tk.Button(frame_entrada, text="Agregar Coordenada", command=agregar_coordenada)
lista_coordenadas = tk.Listbox(frame_entrada, width=20, height=5)

label_x.grid(row=0, column=0)
label_y.grid(row=1, column=0)
entry_x.grid(row=0, column=1)
entry_y.grid(row=1, column=1)
boton_agregar.grid(row=2, column=0)
lista_coordenadas.grid(row=3, column=0, columnspan=2)

boton_eliminar = tk.Button(frame_entrada, text="Eliminar Coordenada", command=eliminar_coordenada, state=tk.DISABLED)
boton_eliminar.grid(row=2, column=1)

label_resultado = tk.Label(frame_resultado, textvariable=resultado)
boton_calcular = tk.Button(frame_resultado, text="Calcular Resultado", command=calcular_resultado)
boton_salir = tk.Button(frame_resultado, text="Salir", command=salir)

label_resultado.pack()
boton_calcular.pack(side=tk.LEFT)
boton_salir.pack(side=tk.RIGHT)

# Cargar la imagen y convertirla a un formato compatible con tkinter
imagen = Image.open("LDTYF.jpg")  # Reemplaza "ejemplo.png" con la ruta de tu imagen
imagen_tk = ImageTk.PhotoImage(imagen)

# Crear un widget Label para mostrar la imagen
label_imagen = tk.Label(ventana, image=imagen_tk)
label_imagen.pack()

ventana.mainloop()
