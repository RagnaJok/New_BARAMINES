import tkinter as tk

root = tk.Tk()

# Définir les couleurs du dégradé
color1 = "#3366ff"
color2 = "#ff3333"

# Créer le dégradé
gradient = tk.Canvas(root, width=100, height=50)
gradient.create_rectangle(0, 0, 100, 50, fill=color1, outline=color1)
gradient.create_rectangle(0, 0, 100, 25, fill=color2, outline=color2)
gradient.pack()

# Créer le bouton
btn = tk.Button(root, text="Mon Bouton", highlightbackground=color1, highlightcolor=color2)
btn.pack()

root.mainloop()
