""" Main Class """
from tkinter import Tk, Canvas
from Map import Map

def main():
    """Main function"""
    window = Tk()
    window.title("McGyver Escape Game")

    canvas = Canvas(window, width=300, height=300)
    canvas.pack()

    mapg = Map("./resources/map.txt", canvas)
    mapg.load_map()
    mapg.paint_map()

    window.bind("<Up>", lambda event, sens='N': mapg.move_macgyver(sens))
    window.bind("<Right>", lambda event, sens='E': mapg.move_macgyver(sens))
    window.bind("<Down>", lambda event, sens='S': mapg.move_macgyver(sens))
    window.bind("<Left>", lambda event, sens='W': mapg.move_macgyver(sens))

    window.mainloop()

main()
