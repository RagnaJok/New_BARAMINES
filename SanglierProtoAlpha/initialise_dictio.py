import json

# exemple de dictionnaire de boisson
drink_data = {'Coca-Cola': {'category': 'Boisson gazeuse', 'price': '2.50'},
              'Pepsi': {'category': 'Boisson gazeuse', 'price': '2.00'},
              'Sprite': {'category': 'Boisson gazeuse', 'price': '2.00'},
              "Jus d'orange": {'category': 'Jus de fruit', 'price': '3.00'}}

# écrire le dictionnaire dans un fichier JSON
with open("drink_data.json", "w") as f:
    json.dump(drink_data, f)
