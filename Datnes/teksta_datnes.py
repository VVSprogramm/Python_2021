#Teksta datņu atvēršana, nolasīšana, aizvēršana

# #1. veids
# file = open("pirmais.txt", "r", encoding="utf-8")
# print(file.read())
# file.close()

# #2.veids
# with open("pirmais.txt", "r", encoding="utf-8") as file:
#     print(file.read())
#     file.close()

# #Līnijas izvade
# file = open("pirmais.txt", "r", encoding="utf-8")
# print(file.readline())
# print(type(file.readline()))
# file.close()

# #Simbolu lasīšana
# file = open("pirmais.txt", "r", encoding="utf-8")
# print(file.read(15))
# file.close()


#Jauna teksta faila izveide

file = open("meginajums.txt", "w", encoding="utf-8")

file.write("Sveiki!")

saturs = ["Ir 2022.gads \n", "Ir 2022.gada 1.februāris\n", "Sveiki vēlreiz!\n"]

file.writelines(saturs)

file.close()

with open("meginajums.txt","r",encoding="utf-8") as file:

    print(file.read())
    print(file.readline())

    file.seek(0) #Pārvietojamies uz faila sākumu

    print(file.readline())

with open("meginajums.txt","a",encoding="utf-8") as file:
    file.write("Es esmu te!\n")

with open("meginajums.txt","w",encoding="utf-8") as file:
    file.write("Kas notika?")