import random
import tkinter as tk
from tkinter import *
from tkinter import messagebox

def loadMap():
	global map, macGyverPos

	# Open map and parse it as 2D Array
	with open('./ressources/map.txt') as file:
		map = [[case for case in line.strip("\n")] for line in file]

	# Set random position for entities (character/item)
	entities = ['M', 'G', '|', '=', '§']
	for i, line in enumerate(map):
		for y, case in enumerate(line):
			if case == '@':
				#entitiesPos.append([entities.pop(random.randrange(len(entities))), i, y])
				#line[y] = entitiesPos[-1][0]
				line[y] = entities.pop(random.randrange(len(entities)))
				if(line[y] == 'M'):
					macGyverPos = [i, y]

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

def moveMacGyver(event, sens):
	global macGyverPos
	if sens == 'N':
		newPos = [macGyverPos[0]-1,macGyverPos[1]]
	if sens == 'E':
		newPos = [macGyverPos[0],macGyverPos[1]+1]
	if sens == 'S':
		newPos = [macGyverPos[0]+1,macGyverPos[1]]
	if sens == 'W':
		newPos = [macGyverPos[0],macGyverPos[1]-1]

	if(map[newPos[0]][newPos[1]] == ' '):
		map[macGyverPos[0]][macGyverPos[1]] = ' '
		map[newPos[0]][newPos[1]] = 'M'
		macGyverPos = newPos
	if(map[newPos[0]][newPos[1]] == 'G'):
		if(tk.messagebox.askyesno("Game Over", "You Win ! Would you start a new game ?")):
			loadMap()
			paintMap()
		else:
			main.quit()

	paintMap()


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
macGyverPos = []

# Loading game
loadMap()
paintMap()

main.bind("<z>", lambda event, sens='N' : moveMacGyver(event, sens))
main.bind("<d>", lambda event, sens='E' : moveMacGyver(event, sens))
main.bind("<s>", lambda event, sens='S' : moveMacGyver(event, sens))
main.bind("<q>", lambda event, sens='W' : moveMacGyver(event, sens))
main.mainloop()