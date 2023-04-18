import tkinter as tk
from tkinter import ttk

# créer une nouvelle fenêtre
root = tk.Tk()

# créer une liste d'options pour la liste déroulante
options = ["Option 1", "Option 2", "Option 3"]

# créer la liste déroulante
combobox = ttk.Combobox(root, values=options)
combobox.pack()

# démarrer la boucle principale de la fenêtre
root.mainloop()