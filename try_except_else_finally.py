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



def askint():
    try:
        val = int(input("Ievadi skaitli:"))
    except:
        print("Izskatās, ka tas nav skaitlis")
        val = int(input("Ievadi skaitli:"))
    finally:
        print("Es te vienmēr būšu")
    print(val)

#askint()


def askint():
    while True:
        try:
            val = int(input("Ievadi skaitli:"))
        except:
            print("Izskatās, ka tas nav skaitlis")
            continue
        else:
            print("Jā, tas ir vesels skaitlis!")
            break
        finally:
            print("Es te vienmēr būšu")
        print(val)

#askint()

