from tkinter import *
from random import randint
import webbrowser

#Variables iniciales
palabras = []
cantPasadas = 0
cantConocidasSeguras = 0
cantEstimadaConocidas = 0
cantPalabrasTotales = 0
palabraActual = ""

#Guardo las palabras en una lista
with open("palabrasEspanol.txt", "r") as f:
    palabras = f.readlines()
    cantPalabrasTotales = len(palabras)


#FUNCIONES
def mostrarNuevaPalabra():
    global palabraActual
    palabraActual = palabras.pop(randint(0, len(palabras)-1))
    labelPalabraActual.config(text = palabraActual)

def actualizarInfoEnVentana():
    labelEstimadoConocidas.config(text= f"Palabras conocidas estimadas: {cantEstimadaConocidas}")
    labelPalabrasPasadas.config(text= f"Palabras pasadas: {cantPasadas}")
    labelConocidasSeguras.config(text= f"Conocidas seguras: {cantConocidasSeguras}")

def funcionLaConozco():
    global cantPasadas
    global cantConocidasSeguras
    global cantEstimadaConocidas
    mostrarNuevaPalabra()
    cantPasadas += 1
    cantConocidasSeguras += 1
    cantEstimadaConocidas = int((cantConocidasSeguras/cantPasadas)*cantPalabrasTotales)
    actualizarInfoEnVentana()

def funcionNoLaConozco():
    global cantPasadas
    global cantEstimadaConocidas
    mostrarNuevaPalabra()
    cantPasadas += 1
    cantEstimadaConocidas = int((cantConocidasSeguras/cantPasadas)*cantPalabrasTotales)
    actualizarInfoEnVentana()

def aprenderPalabra():
    global palabraActual
    url = "https://dle.rae.es/" + palabraActual
    webbrowser.open_new_tab(url)

#Inicio Tkinter y añado título
root = Tk()
root.title("Contador de palabras conocidas")

#Establezco la etiqueta que mostraría una palabra aleatoria
labelPalabraActual = Label(root, font=("Arial", 40), padx = 30, pady = 30)

#Establezco el frame donde aparecen los tres botones
frameBotones = Frame(root)
buttonLaConozco = Button(frameBotones, text="La conozco!", font=("Arial", 25), bg = "#ccffcc", command=funcionLaConozco)
buttonNoLaConozco = Button(frameBotones, text="No la conozco :(", font=("Arial", 25), bg = "#ffcccc", command=funcionNoLaConozco)
buttonAprender = Button(frameBotones, text="Quiero aprenderla! :D", font=("Arial", 25), bg = "#ffff00", command=aprenderPalabra)

#Establezco las etiquetas para los tres datos: Estimado de palabras conocidas, cantidad de palabras pasadas y cantidad de palabras que se marcaron como conocidas
labelEstimadoConocidas = Label(root, text="Palabras conocidas estimadas: ", font=("Arial", 20), bg="#ffcc99")
labelPalabrasPasadas = Label(root, text="Palabras pasadas: ", font=("Arial", 20))
labelConocidasSeguras = Label(root, text="Conocidas seguras: ", font=("Arial", 20))

#Muestro los objetos en la ventana
labelPalabraActual.pack()
frameBotones.pack()
buttonLaConozco.grid(row = 0, column = 0)
buttonNoLaConozco.grid(row = 0,column = 1)
buttonAprender.grid(row = 1, column = 0, columnspan = 2)
labelEstimadoConocidas.pack(pady = (20,0))
labelPalabrasPasadas.pack()
labelConocidasSeguras.pack()

#Inicio el programa mostrando ya una palabra
mostrarNuevaPalabra()

#MainLoop
root.mainloop()