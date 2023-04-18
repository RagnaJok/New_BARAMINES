import tkinter as tk
from tkinter import ttk
from utils import changement_icon

def create_table(frame):
    # Création du tableau pour afficher la carte des boissons
    header = ["Boisson", "Catégorie", "Prix"]
    for col, heading in enumerate(header):
        label = tk.Label(frame, text=heading, font=('Arial', 12, 'bold'), width=15)
        label.grid(row=0, column=col)

    # Données du tableau
    global data
    data = [("Café", "Boisson chaude", "2.50"),
            ("Thé", "Boisson chaude", "2.00"),
            ("Coca-Cola", "Boisson froide", "3.00"),
            ("Jus d'orange", "Boisson froide", "3.50"),
            ("demi de blonde","Bière","5")]

    # Création d'une ligne pour chaque donnée
    for i, row in enumerate(data):
        for j, cell in enumerate(row):
            # Création d'un cadre pour chaque cellule
            cell_frame = tk.Frame(frame, borderwidth=1, relief='ridge')
            cell_frame.grid(row=i+1, column=j, sticky='nsew', padx=5, pady=5)
            
            # Ajout de la donnée dans le cadre
            label = tk.Label(cell_frame, text=cell, font=('Arial', 12))
            label.pack(padx=5, pady=5, expand=True, fill='both')
        
        # Ajout d'un séparateur entre chaque ligne
        sep = ttk.Separator(frame, orient='horizontal')
        sep.grid(row=i+2, column=0, columnspan=3, sticky='ew', padx=5, pady=5)

if __name__ == '__main__':
    # Créer une nouvelle fenêtre
    windowB = tk.Tk()
    windowB.title("Carte des boissons")

    # Ajouter des widgets à la nouvelle fenêtre
    label = tk.Label(windowB, text="Voici la carte des boissons") ##rajouter la date de dernière mise à jour des prix de boissons
    label.pack(padx=20, pady=20)

    # Définition de l'icône de la fenêtre
    changement_icon(windowB)

    # Définir la taille de la fenêtre et la mettre au centre gauche
    width = 1200
    height = 800
    x = (windowB.winfo_screenwidth() // 2) - (width // 2) -60 # (-) permet de le déplacer vers la gauche
    y = (windowB.winfo_screenheight() // 2) - (height // 2) -70 # (-) = vers le haut
    windowB.geometry('{}x{}+{}+{}'.format(width, height, x, y))

    # Création du cadre contenant le tableau
    frame = tk.Frame(windowB)
    frame.pack(fill='both', expand=True)
    frame.place(relx=0.5, rely=0.1, anchor="n")
        
    # Appel de la fonction pour créer le tableau
    create_table(frame)

    # Boucle d'ouverture
    windowB.mainloop()


# def add_drink():
#     # Fonction appelée lors de la soumission du formulaire de saisie d'une boisson
#     # Récupération des valeurs saisies
#     name = name_entry.get()
#     category = category_entry.get()
#     price = price_entry.get()
    
#     # Ajout des données à la liste data
#     data.append((name, category, price))
    
#     # Rafraîchissement du tableau
#     for child in frame.winfo_children():
#         child.destroy()
#     header = ["Boisson", "Catégorie", "Prix"]
#     for col, heading in enumerate(header):
#         label = tk.Label(frame, text=heading, font=('Arial', 12, 'bold'), width=15)
#         label.grid(row=0, column=col)
#     for i, row in enumerate(data):
#         for j, cell in enumerate(row):
#             cell_frame = tk.Frame(frame, borderwidth=1, relief='ridge')
#             cell_frame.grid(row=i+1, column=j, sticky='nsew', padx=5, pady=5)
#             label = tk.Label(cell_frame, text=cell, font=('Arial', 12))
#             label.pack(padx=5, pady=5, expand=True, fill='both')
#         sep = ttk.Separator(frame, orient='horizontal')
#         sep.grid(row=i+2, column=0, columnspan=3, sticky='ew', padx=5, pady=5)

#     # Fermeture de la fenêtre de saisie
#     add_window.destroy()

# def open_add_window(window):
#     # Création de la fenêtre de saisie d'une boisson
#     add_window = tk.Toplevel(window)
#     add_window.title("Ajouter une boisson")
    
#     # Ajout des champs de saisie
#     name_label = tk.Label(add_window, text="Nom de la boisson")
#     name_label.pack()
#     name_entry = tk.Entry(add_window)
#     name_entry.pack()
#     category_label = tk.Label(add_window, text="Catégorie")
#     category_label.pack()
#     category_entry = tk.Entry(add_window)
#     category_entry.pack()
#     price_label = tk.Label(add_window, text="Prix")
#     price_label.pack()
#     price_entry = tk.Entry(add_window)
#     price_entry.pack()
    
#     # Ajout du bouton de soumission
#     submit_button = tk.Button(add_window, text="Ajouter", command=add_drink)
#     submit_button.pack()
