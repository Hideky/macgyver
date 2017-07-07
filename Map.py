import random
import tkinter as tk
from tkinter import *

from Entities import Entities
from Wall import Wall
from Floor import Floor
from MacGyver import MacGyver
from Guardian import Guardian
from Items import Items

class Map:
	def __init__(self, path, canvas):
		self.path = path
		# Loading Ressources once
		self.canvas = canvas
		self.map = []
		self.floorI     = tk.PhotoImage(file="./ressources/floor1.png")
		self.wallI      = tk.PhotoImage(file="./ressources/wall.png")
		self.needleI    = tk.PhotoImage(file="./ressources/needle.png")
		self.rodI       = tk.PhotoImage(file="./ressources/rod.png")
		self.etherI     = tk.PhotoImage(file="./ressources/ether.png")
		self.macGyverI  = tk.PhotoImage(file="./ressources/MacGyver.png")
		self.guardianI  = tk.PhotoImage(file="./ressources/guardian.png")

	def loadMap(self):
		# Open map and parse it as 2D Array
		with open(self.path) as file:
			self.map = [[case for case in line.strip("\n")] for line in file]

		# Set random position for entities (character/item)
		entities = ['M', 'G', '|', '=', '§']
		for i, line in enumerate(self.map):
			for y, case in enumerate(line):
				if case == ' ':
					line[y] = Floor()
				if case == '*':
					line[y] = Wall()
				if case == '@':
					line[y] = entities.pop(random.randrange(len(entities)))
					if(line[y] == 'M'):
						self.macGyver = MacGyver(i, y)
						line[y] = self.macGyver
						continue
					if(line[y] == 'G'):
						line[y] = Guardian(i, y)
						continue
					line[y] = Items(i, y, line[y])


	def paintMap(self):
		self.canvas.delete("all")
		for i, line in enumerate(self.map):
			for y, case in enumerate(line):
				if case.__str__() == '*':
					self.canvas.create_image(y*20+10,i*20+10,image=self.wallI)
				if case.__str__() == ' ':
					self.canvas.create_image(y*20+10,i*20+10,image=self.floorI)
				if case.__str__() == '=':
					self.canvas.create_image(y*20+10,i*20+10,image=self.floorI)
					self.canvas.create_image(y*20+10,i*20+10,image=self.rodI)
				if case.__str__() == '§':
					self.canvas.create_image(y*20+10,i*20+10,image=self.floorI)
					self.canvas.create_image(y*20+10,i*20+10,image=self.etherI)
				if case.__str__() == '|':
					self.canvas.create_image(y*20+10,i*20+10,image=self.floorI)
					self.canvas.create_image(y*20+10,i*20+10,image=self.needleI)
				if case.__str__() == 'M':
					self.canvas.create_image(y*20+10,i*20+10,image=self.floorI)
					self.canvas.create_image(y*20+10,i*20+10,image=self.macGyverI)
				if case.__str__() == 'G':
					self.canvas.create_image(y*20+10,i*20+10,image=self.floorI)
					self.canvas.create_image(y*20+10,i*20+10,image=self.guardianI)

	def moveMacGyver(self, event, sens):
		if sens == 'N':
			newPos = [self.macGyver.getX()-1,self.macGyver.getY()]
		if sens == 'E':
			newPos = [self.macGyver.getX(),self.macGyver.getY()+1]
		if sens == 'S':
			newPos = [self.macGyver.getX()+1,self.macGyver.getY()]
		if sens == 'W':
			newPos = [self.macGyver.getX(),self.macGyver.getY()-1]

		if(self.map[newPos[0]][newPos[1]].__str__() == ' '):
			self.map[self.macGyver.getX()][self.macGyver.getY()] = Floor()
			self.map[newPos[0]][newPos[1]] = self.macGyver
			self.macGyver.setX(newPos[0])
			self.macGyver.setY(newPos[1])
		if(self.map[newPos[0]][newPos[1]].__str__() == 'G'):
			if(tk.messagebox.askyesno("Game Over", "You {state} ! Would you start a new game ?".format(state="Win" if self.map[newPos[0]][newPos[1]].checkMacGyver(self.macGyver) else "Lose"))):
				self.loadMap()
				self.paintMap()
			else:
				quit()
		self.paintMap()