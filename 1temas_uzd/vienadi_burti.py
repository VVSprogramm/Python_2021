"""
Uzraksti funkciju, kura atgriež vērtību True, ja abi dotie vārdi sākas ar vienu burtu.

print(sakas_vienadi("Liela lama")) ------> True
print(sakas_vienadi("Maza Lama")) ------> False
"""

"""
Var noderēt:

metodes:
.split() - sadala teksta mainīgo sarakstā
.lower() 
"""

# def kk():
#     a = 6

#     if a == 5:
#         return True
#     else:
#         return False

# print(kk())

# a = "Maza Lama"

# print(a)

# a = a.lower().split()

# print(a)

# print(type(a))

# a = a.split()

# print(a)

# print(type(a))

def sakas_vienadi(teksts):
    teksts = teksts.lower().split()

    print(teksts)

    if teksts[0][0]==teksts[1][0]:
        return True
    else:
        return False

print(sakas_vienadi("Liela Lama"))
print(sakas_vienadi("maza Lama"))

def sakas_vienadi(teksts):
    teksts = teksts.lower().split()

    return teksts[0][0]==teksts[1][0]
        

print(sakas_vienadi("Liela Lama"))
print(sakas_vienadi("maza Lama"))


