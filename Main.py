import random
import tkinter as tk
from tkinter import *

def loadMap():
	global map

	# Open map and parse it as 2D Array
	with open('./ressources/map.txt') as file:
		map = [[case for case in line.strip("\n")] for line in file]

	# Set random position for entities (character/item)
	entities = ['M', 'G', '|', '=', '§']
	for line in map:
		for i, case in enumerate(line):
			if case == '@':
				line[i] = entities.pop(random.randrange(len(entities)))


def paintMap():
	canvas.delete("all")
	for i, line in enumerate(map):
		for y, case in enumerate(line):
			if case == '*':
				canvas.create_image(y*20+10,i*20+10,image=wall)
			if case == ' ':
				canvas.create_image(y*20+10,i*20+10,image=floor)
			if case == '=':
				canvas.create_image(y*20+10,i*20+10,image=floor)
				canvas.create_image(y*20+10,i*20+10,image=rod)
			if case == '§':
				canvas.create_image(y*20+10,i*20+10,image=floor)
				canvas.create_image(y*20+10,i*20+10,image=ether)
			if case == '|':
				canvas.create_image(y*20+10,i*20+10,image=floor)
				canvas.create_image(y*20+10,i*20+10,image=needle)
			if case == 'M':
				canvas.create_image(y*20+10,i*20+10,image=floor)
				canvas.create_image(y*20+10,i*20+10,image=macGyver)
			if case == 'G':
				canvas.create_image(y*20+10,i*20+10,image=floor)
				canvas.create_image(y*20+10,i*20+10,image=gardien)

# Window
main=Tk()
main.title("McGyver Escape Game")

# Canvas
canvas=Canvas(main, width=300, height=300)
canvas.pack()

# Loading Ressources once
floor    = tk.PhotoImage(file="./ressources/floor1.png")
wall     = tk.PhotoImage(file="./ressources/wall.png")
needle   = tk.PhotoImage(file="./ressources/needle.png")
rod      = tk.PhotoImage(file="./ressources/rod.png")
ether    = tk.PhotoImage(file="./ressources/ether.png")
macGyver = tk.PhotoImage(file="./ressources/MacGyver.png")
gardien  = tk.PhotoImage(file="./ressources/Gardien.png")
map = []

# Loading game
loadMap()
paintMap()

mainloop()
