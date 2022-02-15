#Mainīgais saraksts jeb list

# []

#Mainīgais var saturēt dažādus datu tipus
my_list = ['Teksts', 1, 2]
print(my_list)

#Elementu skaits mainīgajā

print("Saraksa my_list elementu skaits: ", len(my_list))


#index metode 

print(my_list[1])
print(my_list[0:])

#elementa maiņa

my_list[0] = 'Sveiki'
print(my_list)

#elementu pievienošana
print(my_list + ["čau"])
my_list = my_list + ["suns"]
print(my_list)

my_list.append('kaķis')
print(my_list)

#pop
my_list.pop(0)
print(my_list)