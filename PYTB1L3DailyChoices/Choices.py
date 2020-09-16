
print("Je alarm gaat af net optijd voor school. LIG je nog even in bed of STA je op?")
choice = input()
if choice == 'LIG':
    print("Je valt weer in slaap en na 15 minuten schrik je wakker.")
elif choice == 'STA':
    print("Je voelt je heel moe en die 4 uur slaap heeft daar niet bij geholpen")
else:
    print(choice, "is een erg goede keuze")

print("Je krijgt een bericht van je beste vriend. REAgeer je erop of maak je eerst ONTbijt")
choice = input()
if choice == 'REA':
    print("Je praat een tijdje en dan besef je dat je nog maar vrij weining tijd over hebt.")
elif choice == 'ONT':
    print("Je bent optijd en je kan niet wachten om met je beste vriend te praten na je ontbijt.")
else:
    print("Dat kan natuurlijk ook,")

print("een tijd later stap je uit de trein en ben je bijna op school. LOOP je of neem je de FIETS naar school?")
choice = input()
if choice == 'LOOP':
    print("Je loopt relaxed naar school met wat muziek en je bent een kwartier voor de les in het lokaal")
elif choice == 'FIETS':
    print("Je bent erg optijd en nu verveel je je op school.")
else:
    print(choice, "kan ook maar ik zou liever lopen..")

print("Na school kom je net voor etenstijd thuis. EET je eerst een snack of kijk je of er een VRIEND online is?")
choice = input()
if choice == 'EET':
    print("Het is net voor etenstijd.... waarom eet je dan een snack...")
elif choice == 'VRIEND':
    print("Je vriend is online en je praat een tijdje met elkaar.")
else:
    print(choice, "<- Als je slaap zei dan is dat ook een prima keuze, als je wat anders had dan is het geen goede keuze.")

print("Na de training in de avond kom je erg moe thuis. Ga je al gelijk naar BED of PRAAT je op discord tot 4uur snachts ")
choice = input()
if choice == 'BED':
    print("Het is niet 4 uur snachts dus je kan niet in slaap vallen. Je verpest je hele avond. Leuk.")
elif choice == 'PRAAT':
    print("Je praat de hele nacht door en om 4 uur besef je dat je weer over 4 uur op moet staan")
else:
    print("Hm ok ik praat liever.")

print("-----------")
print("Ik weet niet welke keuzes je hebt gemaakt maar ik zou sochtends gelijk opstaan en tijdens het ontbijt praten met vrienden, dan lopen naar school, thuis praat ik weer met vrienden en snachts praat ik ook met vrienden")
