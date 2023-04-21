# New_BARAMINES
Si vous voulez le télécharger, cliquer [ici]([https://github.com/Shaztronix/New_BARAMINES/releases/tag/Sanglier-v0.0.19.3-ProtoAlpha](https://github.com/Shaztronix/New_BARAMINES/archive/refs/tags/Sanglier-v0.0.19.3-ProtoAlpha.zip)) et sortez le de son archive. Ensuite ouvrer Launcher :)



# Fonctionnalités
La construction du nouveau logiciel de gestion du BARAMINES de l'IMT Mines Albi.
Ce qu'il est possible de faire :
- Voir une carte des boissons
- Accès Administrateur ( mot de passe = 123 )
- ce qui permet d'accès aux commandes Ajouter/Supprimer/Editer/Rafraichir la page (seul Ajouter et Rafraichir fonctionne - Rafraichir est inutile enfaite )
- Cela met à jour automatiquement les donnéees de la carte de boissons
- lien entre un fichier .JSON et la carte des boissons afin de ne pas réécrire la carte
- Il y a un launcher dans le dossier principal (Launcher ou Launcher_Dictio) qui permet de lancer directement le logiciel. Juste double-cliquer leeeee.

# Reste à faire : 
PLEINS DE TRUCS
- faire passer le chemin d'accès de l'icone, du SANGLIER et de la carte des boissons en universel (cf Launcher.py)(( # Récupérer le répertoire courant
current_dir = os.getcwd() ))
- faire un dossier avec les images
- faire un dossier de sauvegardes
- Rajouter un titre à chacune des fenêtres
- rendre unique les choix de catégorie dans les Combobox (en cours, fait dans Supprimer)
- Rajouter la date (où ?) de la dernière mise à jour du fichier/ carte des boissons
- et rajouter la fenêtre de prévention si la carte des boissons a été modifié récemment (idée : comparer les dates de dernieres maj de la carte des boissons avec ?)
- Revoir le chemin de la Carte des Boissons sur l'écran d'accueil
