geld = 30.00
spaarpot = 0

print("Geld = 30")
print("Ik koop voor 10 euro eten")
ax = geld - 10.00
print("geld - 10 =", ax )
print("Ik krijg van werk loon")
bx = ax + 120.00
print("geld + 120 =", bx )
print("Ik wil de helft bewaren")
cx = bx / 2
print("geld / 2 =", cx )
print("Je verliest wat geld op staat")
dx = cx % 12
print("geld % 12 =", dx )
print("Je vader doet wat geld in je spaarpot")
spaarpot += 40
print ("spaarpot + 40", spaarpot )
print("Je wilt weten hoeveel geld meer in je spaarpot zit dan dat je zelf hebt")
dx /= spaarpot
print("je hebt ",dx ,"zo veel geld als in je spaarpot")


