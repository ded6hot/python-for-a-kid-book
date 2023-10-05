from tkinter import *
import random

tk = Tk()
canvas = Canvas(tk, width=700, height=700)
canvas.pack()

colors = ('green', 'red', 'blue', 'orange', 'yellow', 'pink', 'purple', 'violet', 'magenta', 'cyan')
def random_rectangle(width, height, colors):
    x1 = random.randrange(width)
    y1 = random.randrange(height)
    x2 = x1 + random.randrange(width)
    y2 = y1 + random.randrange(height)
    color_choice = random.choice(colors)
    canvas.create_rectangle(x1, y1, x2, y2, fill= color_choice)


for x in range(0, 100):
    random_rectangle(400, 400, colors)

Tk.mainloop(canvas)

print(abs(-1000))
a = 1000



