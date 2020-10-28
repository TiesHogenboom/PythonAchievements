ListMaaltijd = ["Ontbijd", "kleine snack", "Lunch", "Avondeten", "Snack snachts"]
print("Mijn maaltijden voor vandaag zijn: ", ListMaaltijd)
print("Dat zijn dus", len(ListMaaltijd), "maaltijden")
print("------------------------------------")
ListMaaltijd.remove("Snack snachts")
ListMaaltijd.insert(5, "Nacht maaltijd")
print("Een snack midden in de nacht is niet genoeg", ListMaaltijd)
print("------------------------------------")
print("Ik neem een kleine snack als", ListMaaltijd.index("kleine snack")+1, "e maaltijd")
