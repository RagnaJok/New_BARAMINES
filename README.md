# New_BARAMINES

La construction du nouveau logiciel de gestion du BARAMINES de l'IMT Mines Albi.
Ce qu'il est possible de faire :
- Voir une carte des boissons
- Accès Administrateur ( mot de passe = 123 )
- ce qui permet d'accès aux commandes Ajouter/Supprimer/Editer/Rafraichir la page (seul Ajouter et Rafraichir fonctionne - Rafraichir est inutile enfaite )
- Cela met à jour automatiquement les donnéees de la carte de boissons
- lien entre un fichier .JSON et la carte des boissons afin de ne pas réécrire la carte
- Il y a un launcher dans le dossier principal (Launcher ou Launcher_Dictio) qui permet de lancer directement le logiciel. Juste double-cliquer leeeee.

Reste à faire : 
PLEINS DE TRUCS
- faire passer le chemin d'accès de l'icone, du SANGLIER et de la carte des boissons en universel (cf Launcher.py)(( # Récupérer le répertoire courant
current_dir = os.getcwd() ))
- faire un dossier avec les images
- faire un dossier de sauvegardes
- Rajouter un titre à chacune des fenêtres
- rendre unique les choix de catégorie dans les Combobox
