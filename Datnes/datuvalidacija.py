while True:
    tel_nr = input("Ievadi savu telefona numuru: ")
    if len(tel_nr) <8:
        continue
    else:
        break


while True:
    vecums = input("Ievadi savu vecumu: ")
    if vecums.isdigit() == True:
        break
    else:
        continue

print(vecums)

while True:
    vards = input("Ievadi savu vārdu: ")
    if vards.strip() == "":
        print("Ievadi vārdu atkārtoti")
        continue
    else:
        break

print(vards)