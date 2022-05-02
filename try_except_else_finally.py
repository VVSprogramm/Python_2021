# try:
#     f = open('testfile','w')
#     f.write('Tests 2')
# except IOError:
#     print("Error: Fails netika atrasts vai nevar tikt nolasīts")
# else:
#     print("Viss sanāca!")
#     f.close()

# f = open('testfile','r')
# f.write('Tests') 



# try:
#     f = open('testfile','a')
#     f.write('Tests 3')
#     f.close()
# finally:
#     print("Es vienmēr te būšu")



# def askint():
#     try:
#         val = int(input("Ievadi skaitli:"))
#     except:
#         print("Izskatās, ka tas nav skaitlis")
#         val = int(input("Ievadi skaitli:"))
#     finally:
#         print("Es te vienmēr būšu")
#     print(val)

# #askint()


# def askint():
#     while True:
#         try:
#             val = int(input("Ievadi skaitli:"))
#         except:
#             print("Izskatās, ka tas nav skaitlis")
#             continue
#         else:
#             print("Jā, tas ir vesels skaitlis!")
#             break
#         finally:
#             print("Es te vienmēr būšu")
#         print(val)

# #askint()




#02.05.

import sys

saraksts = ['a',0,2]

for i in saraksts:
    try:
        print("Skaitlis ir:",i)
        a = 1/int(i)
        break
    except:
        print("Kļūda:",sys.exc_info()[0])
print(a)


for i in saraksts:
    try:
        print("Skaitlis ir:",i)
        a = 1/int(i)
        break
    except Exception as e:
        print("Kļūda:",e.__class__)
print(a)