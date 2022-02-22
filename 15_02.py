#Dati, kurus ievadīs:
#Vārds
#Uzvārds
#Vecums
#Telefona numurs

import json

vards = input("Ievadi vārdu: ")
uzvards = input("Ievadi uzvārdu: ")
vecums = input("Ievadi vecumu: ")
tel_nr = input("Ievadi telefona numuru: ")

#Dati jāsaglabā vārdnīcā ({})

ievad_dati = {
    "Uzvārds":uzvards,
    "Vecums":vecums,
    "Telefona numurs":tel_nr
}

with open("ievaktieDati.json","r", encoding="utf-8") as fails:
    json_data = json.load(fails)

    ir_saraksta =True
    for key in json_data.keys():
        if key == vards:
            break
        if key != vards:
            ir_saraksta = False

    if ir_saraksta == True:
        print("Vārds ir sarakstā")
    else:
        json_data[vards]=ievad_dati

#Savāktie dati jāsaglabā failā ievaktieDati.json

with open("ievaktieDati.json","w", encoding="utf-8") as fails:
    json.dump(json_data,fails, indent = 4, ensure_ascii=False)