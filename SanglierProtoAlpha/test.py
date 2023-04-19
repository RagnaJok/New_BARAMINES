data = [    ["Café", "Boisson chaude", "2.50"],
    ["Thé", "Boisson chaude", "2.00"],
    ["Coca-Cola", "Boisson froide", "3.00"],
    ["Jus d'orange", "Boisson froide", "3.50"],
    ["demi de blonde","Bière","5"]  ]

data3 = []
Name = ['Café','Thé','Coca']
Categorie = ['Beer','Exceptionnel','Soft']
Prix = ['2','7','5']

for i in range(len(Name)):
    New_Drink = [Name[i],Categorie[i],Prix[i]]
    data3.append(New_Drink)
print(data3)
