import random

def original(word):
    randomised = ''.join(random.sample(word, len(word)))
    print(randomised)
    return original
    
original(input("Voer je eerste woord in: "))
original(input("Voer je tweede woord in: "))
original(input("Voer je derde woord in: "))