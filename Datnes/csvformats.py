#Var izmantot iebūvēto moduli csv

import csv

file = open("csv_meg.csv")

print(type(file))

lasit_csv = csv.reader(file)

print(lasit_csv)

#Kolonnu nosaukumi

header = []
header = next(lasit_csv)
print(header)

#Satura nolasīšana

saturs = []
for rinda in lasit_csv:
    saturs.append(rinda)

print(saturs)
print(type(saturs))

file.close()

#jauna faila izveidošana

kolonnuNosaukumi = ['Vārds', '1.atzīme', '2.atzīme']
dati = [['Pēteris',6,8], ['Annika',7,5], ['Viesturis',8,9]]

with open('skolenu_dati.csv', 'w',encoding="utf-8",newline='') as fails:
    csvwrite = csv.writer(fails)
    csvwrite.writerow(kolonnuNosaukumi)
    csvwrite.writerows(dati)

#Ielasi datnes saturu, pārveido to par masīvu
with open('skolenu_dati.csv', 'r',encoding="utf-8") as fails:
    lasit_csv = csv.reader(fails)
    saturs = []
    for rinda in lasit_csv:
        saturs.append(rinda)
    
    #Masīva garums
    print(len(saturs))

    #pirmā elementa saturu
    print(saturs[0])

    #izvadi uz ekrāna masīva pirmo 3 elementu saturu
    for s in range(3):
        print(saturs[s])

#Definē funkciju, kas kā argumentus izmanto datnes nosaukumu un elementa kārtas numuru
#Izvadi attiecīgo elementu

def izvad_funkc(datnesNosaukums, elNumurs):
    with open(datnesNosaukums, 'r',encoding="utf-8") as fails:
        lasit_csv = csv.reader(fails)
        saturs = []
        for rinda in lasit_csv:
            saturs.append(rinda)

        print(saturs[elNumurs])

izvad_funkc("skolenu_dati.csv",1)
