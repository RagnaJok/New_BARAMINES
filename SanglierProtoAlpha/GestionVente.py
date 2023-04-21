import tkinter as tk
import json, os, multiprocessing, subprocess
from utils import changement_icon

def launch_external_app():
    boisson_file = os.path.join(os.path.dirname(__file__), "BoissonAdmin_Dictionnaire.py")
    subprocess.run(["python", boisson_file], creationflags=subprocess.CREATE_NO_WINDOW)

def carte_des_boissons():
    p = multiprocessing.Process(target=launch_external_app)
    p.start()

def Sell():
    a=1

if __name__ == '__main__':
    # Créer une nouvelle fenêtre
    Vente = tk.Tk()
    Vente.title('Gestion des ventes')
    changement_icon(Vente)
    # Définir la taille de la fenêtre et la mettre au centre gauche de l'écran
    width = 1200
    height = 800
    x = (Vente.winfo_screenwidth() // 2) - (width // 2) -60 # (-) permet de le déplacer vers la gauche
    y = (Vente.winfo_screenheight() // 2) - (height // 2) -70 # (-) = vers le haut
    Vente.geometry('{}x{}+{}+{}'.format(width, height, x, y))
    Vente.config()

    Boisson_button = tk.Button(Vente, text="Carte des boissons", command=carte_des_boissons, font=('Century SchoolBook',25))
    Boisson_button.place(relx=0.605,rely=0.85)

    VenteLydia = tk.Button(Vente,text= 'Vente par Lydia',command=Sell,font=('Century SchoolBook',15))
    VenteLydia.place(relx=0.1,rely=0.1)









    Vente.mainloop()