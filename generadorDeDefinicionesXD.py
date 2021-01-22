from tkinter import *
from random import randint
import webbrowser
from juego import *

#Muestro los objetos en la ventana
labelPalabraActual.pack()
frameBotones.pack()
buttonAprender.grid(row = 1, column = 0, columnspan = 2)
labelPalabrasPasadas.pack()

#Inicio el programa mostrando ya una palabra
mostrarNuevaPalabra()

#MainLoop
root.mainloop()
