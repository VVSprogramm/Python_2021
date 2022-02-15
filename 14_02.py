#Definēt funkciju, kuras argumenti ir divi csv failu nosaukumi
#Pārveidot failus masīvos
#Jāsalīdzina masīvu garumi

import csv

def kopa_csv(pirmaisCSV,otraisCSV):
    
    with open(pirmaisCSV, 'r',encoding="utf-8") as fails:
        lasit_csv = csv.reader(fails)
        saturs = []
        for rinda in lasit_csv:
            saturs.append(rinda)

    with open(otraisCSV, 'r',encoding="utf-8") as fails:
        lasit_csv = csv.reader(fails)
        saturs_otrajam = []
        for rinda in lasit_csv:
            saturs_otrajam.append(rinda)

#Ja masīvi ir vienādi
#Tos apvieno un rezultātu saglabā jaunā datnē.
    
    if len(saturs) == len(saturs_otrajam):
        with open('divikopa.csv', 'w',encoding="utf-8",newline='') as fails:
            csvwrite = csv.writer(fails)
            csvwrite.writerows(saturs)
            csvwrite.writerows(saturs_otrajam)

#Salīdzināt pirmās un otrās datnes masīvus, 
# saglabājot tikai atšķirīgos datus

    unikalie = []

    for unik in saturs:
        if unik not in saturs_otrajam:
            unikalie.append(unik)

    print(unikalie)

    unikalie2 = []

    for unik in saturs_otrajam:
        if unik not in saturs:
            unikalie2.append(unik)

    print(unikalie2)

#Salīdzināt pirmās un otrās datnes masīvus, 
# saglabājot tikai vienādos datus

    vienadie = []
    for unik in saturs_otrajam:
        if unik in saturs:
            vienadie.append(unik)
    print(vienadie)


kopa_csv("pirmais.csv","otrais.csv")


#Definē funkciju, kuras argumenti ir divu json failu nosaukumi
#Pārveido failus par vārdnīca

#Abas vārdnīcas apvienot un ierakstīt rezultātu jaunā json failā

#Salīdzināt vārdnīcu atslēgas un izvadīt tikai tos datus, kuri ir atrodami
#vienā no šīm vārdnīcām

#Salīdzināt vārdnīcu atslēgas un izvadīt tikai tos datus, kuri ir atrodami
#abās vārdnīcās



