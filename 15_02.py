#Dati, kurus ievadīs:
#Vārds
#Uzvārds
#Vecums
#Telefona numurs

import json
import datetime

#Datu meklēšana
def kont_mekl():
    mekl_vards = input("Ievadi vārdu, kuru vēlies atrast: ")

    with open("ievaktieDati.json","r", encoding="utf-8") as fails:
        json_data = json.load(fails)

    for key in json_data.keys():
        if key == mekl_vards:
            dati = json_data[key]
            break
        else:
            dati = "Nav sarakstā"
    return dati

        

#Datu validācija
def check_if_text(a):
    if a.strip()=="":
        return True
    else:
        return False
def check_if_digit(a):
    if a.isdigit():
        return True
    else:
        return False
def check_lenght(a):
    if len(a)<8:
        return False
    else:
        return True

def kont_piev():
    
    while True:
        vards = input("Ievadi vārdu: ")
        if check_if_text(vards) or check_if_digit(vards):
            continue
        else:
            break
    while True:
        uzvards = input("Ievadi uzvārdu: ")
        if check_if_text(uzvards) or check_if_digit(uzvards):
            continue
        else:
            break
    while True:
        vecums = input("Ievadi vecumu: ")
        if check_if_digit(vecums):
            break
        else:
            continue
    while True:
        tel_nr = input("Ievadi telefona numuru: ")
        if not check_if_digit(tel_nr) or not check_lenght(tel_nr):
            continue
        else:
            break      
    #Dati jāsaglabā vārdnīcā ({})

    laiks = datetime.datetime.now()
    parv_laiks = laiks.isoformat()

    ievad_dati = {
        "Uzvārds":uzvards,
        "Vecums":vecums,
        "Telefona numurs":tel_nr,
        "Laiks":parv_laiks
    }

    kont_saglabat(vards,ievad_dati)

def kont_saglabat(vards,ievad_dati):
    with open("ievaktieDati.json","r", encoding="utf-8") as fails:
        json_data = json.load(fails)

    ir_saraksta = False
    for key in json_data.keys():
        if key == vards:
            if not isinstance(json_data[vards],list):
                json_data[vards] = [json_data[vards]]
            json_data[vards].append(ievad_dati)
            ir_saraksta = True
            print("key==vards")
            break

    if not ir_saraksta:
        print("nav sarakstā")
        json_data[vards]=ievad_dati

    #Savāktie dati jāsaglabā failā ievaktieDati.json

    with open("ievaktieDati.json","w", encoding="utf-8") as fails:
        json.dump(json_data,fails, indent = 4, ensure_ascii=False)

while True:
    print("\nIzvēlies darbību:")
    print("1 - kontakta pievienošana")
    print("2 - kontakta meklēšana")
    print("3 - iziet")
    izveele = input()

    if izveele == "1":
        kont_piev()
    elif int(izveele) == 2:
        print(kont_mekl())
    elif int(izveele) == 3:
        exit()
    else:
        print("\nIzvēlies kādu no darbībām!")





