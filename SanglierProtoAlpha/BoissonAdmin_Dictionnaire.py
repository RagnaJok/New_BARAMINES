import tkinter as tk
from tkinter import ttk
from utils import changement_icon

def Create_Frame():
    global frame
    frame = tk.Frame(windowB)
    frame.pack(fill='both', expand=True,padx=20,pady=20)
    frame.place(relx=0.4, rely=0.08, anchor="n")

def create_table(frame, drink_data):
    # Création du tableau pour afficher la carte des boissons
    header = ["Boisson", "Catégorie", "Prix"]
    for col, heading in enumerate(header):
        label = tk.Label(frame, text=heading, font=('Century SchoolBook', 12, 'bold'), width=15)
        label.grid(row=0, column=col)

    # Création d'une ligne pour chaque donnée
    for i, drink in enumerate(drink_data):
        row = drink_data[drink]
        print(row)
        # Création d'un cadre pour chaque cellule
        cell_frame1 = tk.Frame(frame, borderwidth=1, relief='ridge')
        cell_frame1.grid(row=i+1, column=0, sticky='nsew', padx=5, pady=5)
        label1 = tk.Label(cell_frame1, text=drink, font=('Arial', 12))
        label1.pack(padx=5, pady=5, expand=True, fill='both')

        cell_frame2 = tk.Frame(frame, borderwidth=1, relief='ridge')
        cell_frame2.grid(row=i+1, column=1, sticky='nsew', padx=5, pady=5)
        label2 = tk.Label(cell_frame2, text=row["category"], font=('Arial', 12))
        label2.pack(padx=5, pady=5, expand=True, fill='both')

        cell_frame3 = tk.Frame(frame, borderwidth=1, relief='ridge')
        cell_frame3.grid(row=i+1, column=2, sticky='nsew', padx=5, pady=5)
        label3 = tk.Label(cell_frame3, text=row["price"], font=('Arial', 12))
        label3.pack(padx=5, pady=5, expand=True, fill='both')

        # Ajout d'un séparateur entre chaque ligne
        sep = ttk.Separator(frame, orient='horizontal')
        sep.grid(row=i+2, column=0, columnspan=3, sticky='ew', padx=5, pady=5)

def update_table(frame, drink_data):
    # Supprimer les anciennes données du tableau
    for widget in frame.winfo_children():
        widget.destroy()

    # Insérer les nouvelles données dans le tableau
    header = ["Boisson", "Catégorie", "Prix"]
    a=1
    for row, (name, drink) in enumerate(drink_data.items(), start=1):
        a+=1
        print(a)
        category = drink["category"]
        price = drink["price"]
        for col, value in enumerate([name, category, price]):
            label = tk.Label(frame, text=value, font=('Century SchoolBook', 12), width=15)
            label.grid(row=row, column=col)

    # Mettre à jour l'en-tête
    for col, heading in enumerate(header):
        label = tk.Label(frame, text=heading, font=('Century SchoolBook', 12, 'bold'), width=15)
        label.grid(row=0, column=col)

def AjoutDrink():
    def Ajouter():
        drink_data[Name_entry.get()] = {'category': Category_entry.get(), 'price': Price_entry.get()}
        print(Name,Categorie,Prix)
        RefreshDrink()
        Modif.destroy()

    def is_number(char):
        # Vérifie si le caractère est un nombre
        return char.isdigit() or char=='.'

    def validate_number(P):
        # Vérifie si la saisie est un nombre
        if not P:
            return True

        for char in P:
           if not is_number(char):
                return False

        return True

    Modif = tk.Toplevel(windowB)
    changement_icon(Modif)
    width = 700
    height = 160
    x = (Modif.winfo_screenwidth() // 2) - (width // 2) -60 # (-) permet de le déplacer vers la gauche
    y = (Modif.winfo_screenheight() // 2) - (height // 2) -70 # (-) = vers le haut
    Modif.geometry('{}x{}+{}+{}'.format(width, height, x, y))

    #Infos à remplir
    global Name_entry,Category_entry,Price_entry
    Name_label = tk.Label(Modif, text="Nom :",font=('Century SchoolBook',12))
    Name_label.place(relx=0.01,rely=0.4)
    Name_entry = tk.Entry(Modif,width=15)
    Name_entry.place(relx=0.1,rely=0.4)

    Category_label = tk.Label(Modif, text="Catégorie :",font=('Century SchoolBook',12))
    Category_label.place(relx=0.29,rely=0.4)
    categories = [drink['category'] for drink in drink_data.values()]
    Category_entry = ttk.Combobox(Modif, values=categories, width=15)
    Category_entry.place(relx=0.45,rely=0.4)
    

    Price_label = tk.Label(Modif, text="Prix :",font=('Century SchoolBook',12))
    Price_label.place(relx=0.69,rely=0.4)
    Price_entry = tk.Entry(Modif,width=15,validate='key')
    Price_entry['validatecommand'] = (Price_entry.register(validate_number),'%P')
    Price_entry.place(relx=0.78,rely=0.4)
    

    Validate = tk.Button(Modif,text='Valider',font=('Century SchoolBook',12),command=Ajouter)
    Validate.place(relx= 0.5,rely=0.9,anchor='s')

def EditDrink():
    a=1

def DeleteDrink():    
    def Supprimer():
        Name.append(Name_entry.get())
        Categorie.append(Category_entry.get())
        Prix.append(Price_entry.get())
        print(Name,Categorie,Prix)
        RefreshDrink()
        Modif.destroy()

    def validate_Name(P):
        # Vérifie si la valeur entrée est dans la liste déroulante
        return P in Name

    def on_combobox_select(event):
        # Fonction appelée lorsque la boisson est sélectionnée dans la liste déroulante
        selected_drink = combobox.get() # Récupère la boisson sélectionnée
        if selected_drink in drink_data:
            # Si la boisson est dans les données de boisson, met à jour les entrées
            Category_entry.set(drink_data[selected_drink]['category'])
            Price_entry.set(drink_data[selected_drink]['price'])

    Modif = tk.Toplevel(windowB)
    changement_icon(Modif)
    width = 700
    height = 160
    x = (Modif.winfo_screenwidth() // 2) - (width // 2) -60 # (-) permet de le déplacer vers la gauche
    y = (Modif.winfo_screenheight() // 2) - (height // 2) -70 # (-) = vers le haut
    Modif.geometry('{}x{}+{}+{}'.format(width, height, x, y))

    #Infos à remplir
    global Name_entry,Category_entry,Price_entry
    Name_label = tk.Label(Modif, text="Nom :",font=('Century SchoolBook',12))
    Name_label.place(relx=0.01,rely=0.4)
    Name_entry = ttk.Combobox(Modif,values=Name,width=13,validate='key')
    Name_entry['validatecommand'] = (Modif.register(validate_Name), '%P')
    Name_entry.place(relx=0.1,rely=0.4)

    combobox_values = list(drink_data.keys())
    combobox = ttk.Combobox(Modif, values=combobox_values, width=20)
    combobox.pack()
    combobox.bind('<<ComboboxSelected>>', on_combobox_select) # Associe la fonction à l'événement de sélection de la liste déroulante


    Category_label = tk.Label(Modif, text="Catégorie :",font=('Century SchoolBook',12))
    Category_label.place(relx=0.29,rely=0.4)
    Category_entry = ttk.Combobox(Modif,values=Categorie,width=15)
    Category_entry.place(relx=0.45,rely=0.4)
    

    Price_label = tk.Label(Modif, text="Prix :",font=('Century SchoolBook',12))
    Price_label.place(relx=0.69,rely=0.4)
    Price_entry = ttk.Combobox(Modif,values=Prix,width=15)
    Price_entry.place(relx=0.78,rely=0.4)
    

    Validate = tk.Button(Modif,text='Valider',font=('Century SchoolBook',12),command=Supprimer)
    Validate.place(relx= 0.5,rely=0.9,anchor='s')

def RefreshDrink():
    update_table(frame,drink_data)

if __name__ == '__main__':
    # Créer une nouvelle fenêtre
    windowB = tk.Tk()
    windowB.title("Carte des boissons - Admin")

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
    Create_Frame()

    # # # RAJOUT DES BOUTONS
    # Ajouter une boisson
    Ajout_button  = tk.Button(windowB, text= "Ajouter une boisson",font=("Century SchoolBook",15),command=AjoutDrink)
    Ajout_button.place(relx=0.72,rely=0.1,anchor="nw")
    # Editer une boisson
    Edit_button  = tk.Button(windowB, text= "Modifier une boisson",font=("Century SchoolBook",15),command=EditDrink)
    Edit_button.place(relx=0.72,rely=0.2,anchor="nw")
    # Supprimer une boisson
    Delete_button  = tk.Button(windowB, text= "Supprimer une boisson",font=("Century SchoolBook",15),command=DeleteDrink)
    Delete_button.place(relx=0.72,rely=0.3,anchor="nw")    
    # Rafaîchir le tableau
    Refresh_Button = tk.Button(windowB,text="Rafraîchir le tableau",font=("Century SchoolBook",15),command=RefreshDrink)
    Refresh_Button.place(relx=0.72,rely=0.4,anchor="nw")
    
    # Données du tableau
    global Name,Categorie,Prix
    Name = ['Café','Thé','Coca']
    Categorie = ['Beer','Exceptionnel','Soft']
    Prix = ['2','7','3']
    
    global drink_data
    drink_data = {'Coca-Cola': {'category': 'Boisson gazeuse', 'price': '2.50'},
              'Pepsi': {'category': 'Boisson gazeuse', 'price': '2.00'},
              'Sprite': {'category': 'Boisson gazeuse', 'price': '2.00'},
              "Jus d'orange": {'category': 'Jus de fruit', 'price': '3.00'}}

    # # Création d'une ligne pour chaque donnée
    # for i, row in enumerate(data):
    #     for j, cell in enumerate(row):
    #         # Création d'un cadre pour chaque cellule
    #         cell_frame = tk.Frame(frame, borderwidth=1, relief='ridge')
    #         cell_frame.grid(row=i+1, column=j, sticky='nsew', padx=5, pady=5)
            
    #         # Ajout de la donnée dans le cadre
    #         label = tk.Label(cell_frame, text=cell, font=('Arial', 12))
    #         label.pack(padx=5, pady=5, expand=True, fill='both')
        
    #     # Ajout d'un séparateur entre chaque ligne
    #     sep = ttk.Separator(frame, orient='horizontal')
    #     sep.grid(row=i+2, column=0, columnspan=3, sticky='ew', padx=5, pady=5)

    # Appel de la fonction pour créer le tableau
    create_table(frame,drink_data)

    # Boucle d'ouverture
    windowB.mainloop()