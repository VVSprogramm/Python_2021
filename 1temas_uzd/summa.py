"""
True:
abu skaitļu summa ir 20
viens no skaitļiem ir 20
False:
visi citi gadījumi

print(summa(10,10)) ------ > True
print(summa(10,20)) ------ > True
print(summa(5,5)) ---------> False
"""

'''
or
'''

def summa(a,b):
    return (a+b)==20 or a==20 or b==20

print(summa(5,5))
print(summa(10,10))
print(summa(20,20))

def summa(a,b):
    if (a+b)==20:
        return True
    elif a==20:
        return True
    elif b==20:
        return True
    else:
        return False
