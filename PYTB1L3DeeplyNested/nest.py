#Als ik honger heb en ik geen zin heb om te koken dan bestel ik pizza
#tenzij er nog een kliekje in de koelkast ligt. Dan eet ik die op.
#Als ik geen geld heb ga ik toch koken.
hongerig = True
geenZinInKoken = True
geld = 12
kliekjeInKoelkast = False

print("----------------------------")
if hongerig == True and geld > 10:
    if geenZinInKoken == True:
        if kliekjeInKoelkast == True:
            print("EetKliekje")
        else:
            print("bestelPizza")
if geld < 10:
    print("Koken")
print("----------------------------")
    

