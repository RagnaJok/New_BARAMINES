from tkinter import *

fenetre = Tk()

canvas = Canvas(fenetre, width=3000, height=3000)
canvas.pack()

for i in range(3000):
    r = int(255 * i / 3000)
    g = int(255 * (3000 - i) / 3000)
    b = 0
    couleur = "#%02x%02x%02x" % (r, g, b)
    canvas.create_line(0, i, 3000, i, fill=couleur)
canvas.create_text(200, 200, text="Hello World!", fill="white", font=("Arial", 24))
fenetre.mainloop()