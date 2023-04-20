import tkinter as tk
import json

# exemple de dictionnaire de boisson
drink_dict = {
    "Coca-Cola": {"price": 2.0, "quantity": 10},
    "Pepsi": {"price": 1.5, "quantity": 15},
    "Orangina": {"price": 2.5, "quantity": 5}
}

# écrire le dictionnaire dans un fichier JSON
with open("drink_data.json", "w") as f:
    json.dump(drink_dict, f)

# Création de la fenêtre principale
root = tk.Tk()

# Ouverture du fichier texte
with open("drink_data.json", 'r') as f:
    content = json.load(f)
    print(content)
    print(type(content))

# Création d'un label avec le contenu du fichier
label = tk.Label(root, text=content)
label.pack()

# Affichage de la fenêtre principale
root.mainloop()