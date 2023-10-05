from tkinter import *
import random

tk = Tk()
canvas = Canvas(tk, width=700, height=700)
canvas.pack()

canvas.create_arc(10, 10, 200, 100, extent=45, style=ARC)





Tk.mainloop(canvas)
