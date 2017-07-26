"""Map Class"""
import random
from tkinter import PhotoImage, messagebox
from Wall import Wall
from Floor import Floor
from MacGyver import MacGyver
from Guardian import Guardian
from Items import Items

class Map:
    """Representing a 2D table of the map's game"""
    def __init__(self, path, canvas):
        self.path = path
        # Loading Ressources once
        self.canvas = canvas
        self.map = []
        self.macgyver = None
        self.floor_i = PhotoImage(file="./resources/floor1.png")
        self.wall_i = PhotoImage(file="./resources/wall.png")
        self.needle_i = PhotoImage(file="./resources/needle.png")
        self.rod_i = PhotoImage(file="./resources/rod.png")
        self.ether_i = PhotoImage(file="./resources/ether.png")
        self.macgyver_i = PhotoImage(file="./resources/MacGyver.png")
        self.guardian_i = PhotoImage(file="./resources/guardian.png")

    def load_map(self):
        """Read map from file and transform all char into object"""
        # Open map and parse it as 2D Array
        with open(self.path) as file:
            self.map = [[case for case in line.strip("\n")] for line in file]

        # Set random position for entities (character/item)
        for i, line in enumerate(self.map):
            for y, case in enumerate(line):
                if case == ' ':
                    line[y] = Floor()
                if case == '*':
                    line[y] = Wall()
                if line[y] == 'M':
                    self.macgyver = MacGyver(i, y)
                    line[y] = self.macgyver
                    continue
                if line[y] == 'G':
                    line[y] = Guardian(i, y)
                    continue

        items = ['|', '=', '§']
        while items:
            rand_x = random.randrange(len(self.map))
            rand_y = random.randrange(len(self.map[0]))
            if self.map[rand_x][rand_y].__str__() != ' ':
                continue
            self.map[rand_x][rand_y] = Items(rand_x, rand_y, items.pop())


    def paint_map(self):
        """Paint actual Map on the Canvas"""
        self.canvas.delete("all")
        for i, line in enumerate(self.map):
            for y, case in enumerate(line):
                if case.__str__() == '*':
                    self.canvas.create_image(y*20+10, i*20+10, image=self.wall_i)
                if case.__str__() == ' ':
                    self.canvas.create_image(y*20+10, i*20+10, image=self.floor_i)
                if case.__str__() == '=':
                    self.canvas.create_image(y*20+10, i*20+10, image=self.floor_i)
                    self.canvas.create_image(y*20+10, i*20+10, image=self.rod_i)
                if case.__str__() == '§':
                    self.canvas.create_image(y*20+10, i*20+10, image=self.floor_i)
                    self.canvas.create_image(y*20+10, i*20+10, image=self.ether_i)
                if case.__str__() == '|':
                    self.canvas.create_image(y*20+10, i*20+10, image=self.floor_i)
                    self.canvas.create_image(y*20+10, i*20+10, image=self.needle_i)
                if case.__str__() == 'M':
                    self.canvas.create_image(y*20+10, i*20+10, image=self.floor_i)
                    self.canvas.create_image(y*20+10, i*20+10, image=self.macgyver_i)
                if case.__str__() == 'G':
                    self.canvas.create_image(y*20+10, i*20+10, image=self.floor_i)
                    self.canvas.create_image(y*20+10, i*20+10, image=self.guardian_i)
                self.canvas.create_text(35, 10, text="Backpack: "+str(len(self.macgyver.get_backpack())), fill="#FFF")

    def move_macgyver(self, sens):
        """Move the macgyver entity on the map"""
        if sens == 'N':
            new_pos = [self.macgyver.get_x()-1, self.macgyver.get_y()]
        if sens == 'E':
            new_pos = [self.macgyver.get_x(), self.macgyver.get_y()+1]
        if sens == 'S':
            new_pos = [self.macgyver.get_x()+1, self.macgyver.get_y()]
        if sens == 'W':
            new_pos = [self.macgyver.get_x(), self.macgyver.get_y()-1]

        if type(self.map[new_pos[0]][new_pos[1]]).__name__ == "Items":
            self.macgyver.add_to_backpack(self.map[new_pos[0]][new_pos[1]])
            self.map[new_pos[0]][new_pos[1]] = Floor()

        if self.map[new_pos[0]][new_pos[1]].__str__() == ' ':
            self.map[self.macgyver.get_x()][self.macgyver.get_y()] = Floor()
            self.map[new_pos[0]][new_pos[1]] = self.macgyver
            self.macgyver.set_x(new_pos[0])
            self.macgyver.set_y(new_pos[1])
        if self.map[new_pos[0]][new_pos[1]].__str__() == 'G':
            if self.map[new_pos[0]][new_pos[1]].check_macgyver(self.macgyver):
                state = "Win"
            else:
                state = "Lose"
            if messagebox.askyesno("Game Over", "You "+state+" ! Would you start a new game ?"):
                self.load_map()
                self.paint_map()
            else:
                quit()
        self.paint_map()
