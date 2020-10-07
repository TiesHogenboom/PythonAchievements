Weekdag = "Woensdag"

dag1 = "Je moet vandaag naar school toe. " + "Mis je bus niet.."

dag2 = "Online les! " + "probeer wakker te blijven.."
   
dag3 = "Een vrije dag!"

if Weekdag == "Maandag":
    print(dag1)
elif Weekdag == "Dinsdag":
    print(dag2)
elif Weekdag == "Woensdag":
    print(dag1)
elif Weekdag == "Donderdag":
    print(dag2)
elif Weekdag == "Vrijdag":
    print(dag2)
else:
    print(dag3)
