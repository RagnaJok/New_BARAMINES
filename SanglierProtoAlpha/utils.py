import tkinter as tk

# Personnaliser l'icone de la fenetre
def changement_icone(window):
    from PIL import Image, ImageTk
    image = Image.open("C:/Users/jo/Documents/Cours/M1/BARAMINES/NewSoftware/logo_provisoire.png")
    photo = ImageTk.PhotoImage(image)
    window.iconphoto(True,photo)

def changement_icon(window):
    window.iconbitmap("C:/Users/jo/Documents/Cours/M1/BARAMINES/NewSoftware/logo_provisoire.ico")