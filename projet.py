from module_somme import Somme,produit
nombre_1 = int(input("entrer un premier nombre : "))
nombre_2 = int(input("entrer un deuxieme nombre : "))
liste = ["Somme", "produit"]
choix = input(f"quelles oprations souhaitez vous effectuer : {liste}")
if choix == liste[0] :
    result = Somme(x=nombre_1, y=nombre_2)
    print(f"la somme de ces nombres est : {result}")
else :
    resultat = produit(x=nombre_1, y=nombre_2)
    print(f"la produit de ces nombres est : {resultat}")
    