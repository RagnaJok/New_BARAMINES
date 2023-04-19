import subprocess, os
# obtenir le chemin absolu du fichier en cours d'exécution
dir_path = os.path.dirname(os.path.realpath(__file__))

# chemin relatif vers le fichier de données
data_file = os.path.join(dir_path, 'SanglierProtoAlpha', 'Accueil_Baramines_Dictio.py')

subprocess.Popen(['pythonw', data_file], creationflags=subprocess.CREATE_NO_WINDOW)