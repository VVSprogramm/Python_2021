import json

#Kaut kāda vārdnīca
vardnica = {
    "Vārds":"Jānis",
    "Izglītība":"Vidējā",
    "Vecums":45
    }

#Pārveidot Python uz JSON
a = json.dumps(vardnica)

print(a)

#Pārveidot JSON uz Python
b = json.loads(a)

print(json.dumps(["kivi", "citrons"]))

#dict - Object
#list - Array
#tuple - Array
#str - String
#int - Number
#float - Number
#True - true
#False - false
#None - null

py_data = {
    "Vards":"Annnika",
    "Vecums":30,
    "Dzivs":True,
    "NeDzivs":False,
    "Berni":("Gatis","Anna"),
    "Dzivnieki":None,
    "Masinas":[
        {"Modelis":"Ford Focus", "Gads":2007},
        {"Modelis":"Audi A6", "Gads":2010}
    ]
}

print(json.dumps(py_data, indent=4, separators=(".", "=")))

with open("pirmais_json.json","w", encoding="utf-8") as fails:
    json.dump(py_data,fails, indent = 4, ensure_ascii=False)

with open("pirmais_json.json","r", encoding="utf-8") as fails:
    json_dati = json.load(fails)

    #Vārdnīcas garums
    print(len(json_dati))

    #Visas ataslēgas
    print(json_dati.keys())

    #Visas vērtības
    print(json_dati.values())

    #Pārbaudi, vai dotā atslēga ir vārdnīcā un izvadi tās vērtību
    atsl1 = "Vecums"
    atsl_par = ""
    for atslega in json_dati.keys():
        if atslega == atsl1:
            atsl_par = atslega
            print(json_dati[atslega])
    if atsl1 != atsl_par:
        print(f"Izskatās, ka {atsl1} nav sarakstā")


#Nodefinēt funkciju, kura kā argumentus izmantos 
# datnes nosaukumu un atslēgas nosaukumu
#jāizvada atslēgas vērtība
def datnes_las (datnesNosaukumu, atslega):
    with open(datnesNosaukumu,"r", encoding="utf-8") as fails:
        json_dati = json.load(fails)
        for key in json_dati.keys():
            if key == atslega:
                print(json_dati[atslega])
                return
            else:
                break
        print("Nav atslēgas")

datnes_las("json_dati","Vecums")



