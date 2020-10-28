import random

def original(word):
    randomised = ''.join(random.sample(word, len(word)))
    return original
    
print(original(input("Voer je eerste woord in: ")))
print(original(input("Voer je tweede woord in: ")))
print(original(input("Voer je derde woord in: ")))