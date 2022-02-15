"""
Uzraksti funkciju, kura atgriež mazāko skaitli, ja abi skaitļi ir pāra skaitļi
Atgriež lielāko skaitli, ja abi skaitļi ir nepāra vai viens no skaitļiem ir nepāra skaitlis

print(atgriez_skaitli(2,4)) ------ > 2
print(atgriez_skaitli(2,5)) ------ > 5
"""

'''
4%2=0
min()
max()

return 
'''
def atgriez_skaitli(a,b):

    #Pirmā pārbaude - vai a ir pāra skaitlis

    if a%2 == 0:

        #Otrā pārbaude - vai b ir pāra skaitlis

        if b%2 == 0:
            if a<b:
                return a
            else:
                return b

        #Vai b ir nepāra skaitlis

        if b%2 != 0:
            if a>b:
                return a
            else:
                return b
    else:
        if a>b:
                return a
        else:
                return b

print(atgriez_skaitli(2,4)) 
print(atgriez_skaitli(5,6)) 
    
def atgriez_skaitli(a,b):

    #Pirmā pārbaude - vai a un b ir pāra skaitļi

    if a%2 == 0 and b%2 == 0:

            if a<b:
                return a
            else:
                return b

    else:
        if a>b:
                return a
        else:
                return b

print(atgriez_skaitli(2,4)) 
print(atgriez_skaitli(5,6)) 


def atgriez_skaitli(a,b):

    #Pirmā pārbaude - vai a un b ir pāra skaitļi

    if a%2 == 0 and b%2 == 0:

        return min(a,b)

    else:
        return max(a,b)

print(atgriez_skaitli(2,4)) 
print(atgriez_skaitli(5,6))


