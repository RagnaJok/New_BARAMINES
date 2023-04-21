import tkinter as tk
from tkinter import messagebox
import subprocess, os, multiprocessing
from utils import changement_icon
from datetime import datetime

def on_closing():
    pass

def Quitter():
    window.destroy()

def launch_external_app():
    boisson_file = os.path.join(os.path.dirname(__file__), "Boisson.py")
    subprocess.run(["python", boisson_file], creationflags=subprocess.CREATE_NO_WINDOW)

def launch_external_app_Admin():
    boisson_file = os.path.join(os.path.dirname(__file__), "BoissonAdmin_Dictionnaire.py")
    subprocess.run(["python", boisson_file], creationflags=subprocess.CREATE_NO_WINDOW)

def Vente():
    GestionVente = os.path.join(os.path.dirname(__file__), "GestionVente.py")
    subprocess.run(["python", GestionVente], creationflags=subprocess.CREATE_NO_WINDOW)

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
    password_entry.focus_set()

    validate_button = tk.Button(Admin, text="Valider", command=check_password)
    validate_button.pack(pady=5)
    password_entry.bind('<Return>', on_enter)

if __name__ == '__main__':
    # Créer la fenêtre
    window = tk.Tk()
    window.protocol("WM_DELETE_WINDOW",on_closing)
    window.title("Accueil Baramines")
    label_accueil = tk.Label(window, text="Sanglier V.ProtoAlpha", font=('Century SchoolBook',40))
    label_accueil.place(relx=0.2,rely=0)
    
    ## DATE DERNIERE MAJ
    date_path = os.path.join(os.path.dirname(__file__), "Accueil_Baramines_Dictio.py")

    # Récupération de la date de dernière modification
    mod_time = os.path.getmtime(date_path)
    mod_date = datetime.fromtimestamp(mod_time).strftime("%Y-%m-%d %H:%M")

    date_label = tk.Label(window, text="Dernière mise à jour : " + mod_date)
    date_label.place(relx=0.77, rely=0.96)



    # Définition de l'icône de la fenêtre
    changement_icon(window)

    # Définir la taille de la fenêtre et la mettre au centre gauche de l'écran
    width = 1200
    height = 800
    x = (window.winfo_screenwidth() // 2) - (width // 2) -60 # (-) permet de le déplacer vers la gauche
    y = (window.winfo_screenheight() // 2) - (height // 2) -70 # (-) = vers le haut
    window.geometry('{}x{}+{}+{}'.format(width, height, x, y))
    window.config()

    # Afficher une image de sanglier
    Sanglier = tk.PhotoImage(file='C:\\Users\\jo\\Documents\\Cours\\M1\\BARAMINES\\NewSoftware\\SANGLIER.png')
    SanglierImage = tk.Label(window,image=Sanglier)
    SanglierImage.place(relx=0.1,rely=0.20)

    Boisson_button = tk.Button(window, text="Carte des boissons", command=carte_des_boissons, font=('Century SchoolBook',25))
    Boisson_button.place(relx=0.605,rely=0.85)
    
    Admin_Button = tk.Button(window, text='Administrateur', command=PassAdmin, font=('Century SchoolBook',25))
    Admin_Button.place(relx=0.1,rely=0.85)

    ExitButton = tk.Button(window,text='Enregistrer et quitter la session',command=Quitter, font=('Century SchoolBook',15))
    ExitButton.place(relx=0.505,rely=0.125)

    Vente_Button = tk.Button(window,text='Mode Vente',command=Vente,font=('Century SchoolBook',20))
    Vente_Button.place(relx=0.201,rely=0.108)

    # Lancer la boucle principale d'événements
    window.mainloop()
