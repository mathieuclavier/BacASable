import tkinter as tk 

state = {}

win = tk.Tk()
canvas = tk.Canvas(win, width=300, height=300, background="white")

canvas.pack()

class color():
    def __init__(self,r,g,b):
        self.r = r
        self.g = g
        self.b = b

def set_pixel(x,y,c):
    t = canvas.create_rectangle(x,y,x,y, fill="black")
    