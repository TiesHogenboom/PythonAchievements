geld = 30.00
spaarpot = 0

print("Geld = 30")
print("Ik koop voor 10 euro eten")
geld -= 10.00
print("geld - 10 =", geld )
print("Ik krijg van werk loon")
geld += 120.00
print("geld + 120 =", geld )
print("Ik wil de helft bewaren")
geld /= 2
print("geld / 2 =", geld )
print("Je verliest wat geld op staat")
geld %= 12
print("geld % 12 =", geld )
print("Je vader doet wat geld in je spaarpot")
spaarpot += 40
print ("spaarpot + 40 =", spaarpot )
geld /= spaarpot
print("je hebt ", geld ,"zo veel geld als in je spaarpot")
geld += 9.75
print ("Je verdubbeld je geld in de casino.")
geld *= 2
print ("geld * 2 =", geld)
print ("Je wilt weten hoeveel geld je in totaal hebt")
geld += spaarpot
print ("Je hebt in totaal", geld ,"euro")

print(12 * 12)
print(12 / 2)
print(12 + 12)
print(12 - 2)
print(12 % 2)
print(12 * 10 / 2 + 100 - 10 % 10)