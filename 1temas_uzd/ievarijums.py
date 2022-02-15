# Problēma: Vecvecākiem nepieciešams aprēķināt ievārījuma izmaksas
# 1. specifikācija
# Uzrakstīt funkciju, kas aprēķina ābolu ievārījuma izmaksas
#ievaddati: cukura cena kilogramā, cukura ābolu un garšvielu daudzums, ābolu daudzums kg

recepte = {"cukurs":0.6, "kanelis":0.008,"āboli":2.0, "ūdeni":0.2 }
cena = {"cukurs":0.75, "kanelis":0.3,"āboli":0.0, "ūdeni":0.0 }

def izmaksas_receptei(recepte,cena):
    #Funkcija aprēķina receptes izmaksas
    #Summējot visu sastāvdaļu izmaksas

    summa=0
    for sastavdala in recepte:
        daudzums = recepte[sastavdala]
        summa += daudzums *cena[sastavdala]
    return summa

def izmaksas_kopa(abolu_svars, recepte,cena):
    #Funkcija aprēķina izmaksas dotam daudzumam ābolu

    #izmaksas uz vienu kg ābolu

    izmaksas_kg = izmaksas_receptei(recepte,cena)/recepte['āboli']

    #Izmaksas uz doto ābolu daudzumu

    ievarijuma_izmaksas = abolu_svars * izmaksas_kg

    print("Uz {} kg ābolu izmaksas būs {:.2f} EUR ".format(abolu_svars,ievarijuma_izmaksas))

izmaksas_kopa(15,recepte,cena)


