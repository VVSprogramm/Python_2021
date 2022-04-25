# masivs = [1,2,3,4,5]

# summa = 0

# for i in range(len(masivs)):
#     summa += masivs[i]

# print(summa)

# Sula veikalā maksā 1.50 eiro (bez PVN) un siers 3 eiro (bez PVN). 
# Aprēķini, cik kopā tev ir jāmaksā par pirkumu ar PVN!

#Testēšanas plāns 
#Sula ar PVN 1.815
#Siers ar PVN 3.63
#5.445
 
PVN = 0.21
 
sulasCena = 1.50
sulasPVN = sulasCena * PVN
 
sieraCena = 3.00
sieraPVN = sieraCena * PVN
 
print(sulasCena + sulasPVN + sieraCena + sieraPVN)
print()