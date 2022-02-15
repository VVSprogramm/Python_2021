#Mainīgais bibliotēka

# {}, katrai vērtībai ir sava atslēga

pirmais = {'atsl1':'vert1', 'atsl2':'vert2'}
print(pirmais)

print(pirmais['atsl1'])

otrais = {'atsl1':[1,2,3], 'atls2':'Teksts', 'atsl3':5}

print(otrais['atsl1'],otrais['atsl3'])

tresais = {'Mācību priekšmeti':{'Matemātika':5, "Latviešu valoda":[6, 8, 5], "Programmēšana":4}}

print(tresais["Mācību priekšmeti"]["Latviešu valoda"][2])

tresais['Mācību priekšmeti']['Matemātika'] = [5,'upe']
print(tresais)

#Tukšas bibliotēkas izveide

pirmais = {}
pirmais['koks'] = 'bērzs'
pirmais ['ūdenstilpne'] = 'upe'

print(pirmais)

print(pirmais.keys())
print(pirmais.values())

print(pirmais.items())