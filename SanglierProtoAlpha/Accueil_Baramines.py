import tkinter as tk
from tkinter import messagebox
import subprocess, os, multiprocessing
from utils import changement_icon
import tkinter.font as tkFont


def launch_external_app():
    boisson_file = os.path.join(os.path.dirname(__file__), "Boisson.py")
    subprocess.run(["python", boisson_file], creationflags=subprocess.CREATE_NO_WINDOW)

def launch_external_app_Admin():
    boisson_file = os.path.join(os.path.dirname(__file__), "BoissonAdmin.py")
    subprocess.run(["python", boisson_file], creationflags=subprocess.CREATE_NO_WINDOW)

def carte_des_boissons():
    p = multiprocessing.Process(target=launch_external_app)
    p.start()

def PassAdmin():
    def check_password():
        password = "123"
        if password_entry.get() == password:
            p = multiprocessing.Process(target=launch_external_app_Admin)
            p.start()
            password_entry.delete(0, 'end')
            Admin.destroy()
           
        else:
            # Afficher un message d'erreur si le mot de passe est incorrect
            messagebox.showerror("Mot de passe incorrect", "Le mot de passe que vous avez entré est incorrect. Veuillez réessayer.")
    def on_enter(event):
        validate_button.invoke()
    
    Admin = tk.Toplevel(window)
    changement_icon(Admin)
    width = 200
    height = 150
    x = (Admin.winfo_screenwidth() // 2) - (width // 2) -60 # (-) permet de le déplacer vers la gauche
    y = (Admin.winfo_screenheight() // 2) - (height // 2) -70 # (-) = vers le haut
    Admin.geometry('{}x{}+{}+{}'.format(width, height, x, y))



    password_label = tk.Label(Admin, text="Mot de passe:")
    password_label.pack(pady=5)
    password_entry = tk.Entry(Admin, show="*")
    password_entry.pack(pady=5)

    validate_button = tk.Button(Admin, text="Valider", command=check_password)
    validate_button.pack(pady=5)
    password_entry.bind('<Return>', on_enter)


 # Fonction pour afficher le choix sélectionné
def print_choice():
    selection = listbox.curselection()
    if selection:
        index = selection[0]
        value = listbox.get(index)
        print("Choix sélectionné :", value)

        
if __name__ == '__main__':
    # Créer la fenêtre
    window = tk.Tk()
    window.title("Accueil Baramines")
    label_accueil = tk.Label(window, text="Sanglier V.ProtoAlpha", font=('Century SchoolBook',40))
    label_accueil.pack(padx=20,pady=20)
    
    # Définition de l'icône de la fenêtre
    changement_icon(window)

    # Définir la taille de la fenêtre et la mettre au centre gauche de l'écran
    width = 1200
    height = 800
    x = (window.winfo_screenwidth() // 2) - (width // 2) -60 # (-) permet de le déplacer vers la gauche
    y = (window.winfo_screenheight() // 2) - (height // 2) -70 # (-) = vers le haut
    window.geometry('{}x{}+{}+{}'.format(width, height, x, y))
    window.config()

    # Créer une liste de choix
    choices = ["Choix 1", "Choix 2", "Choix 3"]
    frame = tk.Frame(window)
    frame.pack(pady=10)
    frame.place(x=20, y=20)
    frame.config(width=100, height=75, borderwidth=2, relief=tk.SOLID)

    listbox = tk.Listbox(frame)  # Ajouter la liste à l'intérieur du cadre
    for choice in choices:
        listbox.insert(tk.END, choice)
    listbox.pack()  # Utiliser pack() sur le cadre, pas sur la liste    
    #print("Dimensions de la liste de choix : ", listbox.winfo_width(), listbox.winfo_height())

    # Ajouter un champ d'entrée pour le mot de passe
    password_label = tk.Label(window, text="Mot de passe:")
    password_label.pack(pady=5)
    password_entry = tk.Entry(window, show="*")
    password_entry.pack(pady=5)

    # validate_button = tk.Button(window, text="Valider", command=check_password)
    # validate_button.pack(pady=5)

    Boisson_button = tk.Button(window, text="Carte des boissons", command=carte_des_boissons, font=('Century SchoolBook',25))
    Boisson_button.place(x=width-480,y=120)
    
    Admin_Button = tk.Button(window, text='Administrateur', command=PassAdmin, font=('Century SchoolBook',15))
    Admin_Button.place(w=width-480,y=500)


   

    # Empêcher le cadre de la liste de choix de s'étendre
    frame.pack_propagate(False)

    # Lancer la boucle principale d'événements
    window.mainloop()
