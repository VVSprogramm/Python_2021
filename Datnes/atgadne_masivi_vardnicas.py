# Masīvs jeb list 

#[]
#Pirmais indekss ir 0
#Lai piekļūtu vērtībai, ir nepieciešams zināt indeksu
#Masīva garums NAV masīva pēdējais indekss
#Masīva pēdējais indekss = masīva garums - 1

'''
Vērtība | A | B | C | D | E | F |
Indekss | 0 | 1 | 2 | 3 | 4 | 5 |
'''

masivs = ["A", "B", "C", "D", "E", "F"]

print(masivs)
print(type(masivs))
print(masivs[3])

for x in masivs:
    print(x)


#Vārdnīca jeb dictionary

#{}
#Katrai vērtībai ir sava atslēga

'''
Atslēga | Vārds | Izglītība | Vecums |
Vērtība | Jānis |   Vidējā  |   45   |
'''

vardnica = {
    "Vārds":"Jānis",
    "Izglītība":"Vidējā",
    "Vecums":45
    }

print(vardnica)
print(type(vardnica))
print(vardnica["Vārds"])


#Kombinācija - vārdnīca masīvā

personas = [
    {"Vārds":"Jānis","Izglītība":"Vidējā","Vecums":45},
    {"Vārds":"Viesturis","Izglītība":"Augstākā","Vecums":27}
]

print(type(personas))

for persona in personas:
    print(persona["Vārds"])