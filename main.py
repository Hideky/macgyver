import random
import tkinter as tk
from tkinter import *
from tkinter import messagebox
from Map import Map

# Window
main=Tk()
main.title("McGyver Escape Game")

# Canvas
canvas=Canvas(main, width=300, height=300)
canvas.pack()

map = Map("./resources/map.txt", canvas)
macGyverPos = []

# Loading game
map.loadMap()
map.paintMap()

main.bind("<z>", lambda event, sens='N' : map.moveMacGyver(event, sens))
main.bind("<d>", lambda event, sens='E' : map.moveMacGyver(event, sens))
main.bind("<s>", lambda event, sens='S' : map.moveMacGyver(event, sens))
main.bind("<q>", lambda event, sens='W' : map.moveMacGyver(event, sens))
main.mainloop()
