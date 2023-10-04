import time


def hello():
    print('hello')


def person(width, height):
    print("Моя ширина - %s, а висота - %s" % (width, height))


# region Button
from tkinter import *

tk = Tk()
btn = Button(tk, text="надми на мене", command=hello)
btn.pack()
# endregion

tk = Tk()
tk.title('canvas')
canvas = Canvas(tk, width=500, height=500)
canvas.pack()
canvas.create_line(0, 0, 500, 500)
canvas.create_rectangle(10, 10, 50, 300)

tk.update()
Tk.mainloop(canvas)
while 1:
    tk.update_idletasks()
    tk.update()
    time.sleep(0.01)