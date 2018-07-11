lista = [["a", "b", "c", "d", "e", "f"], [1, 2, 3]]

print(lista[0:3])
print(lista[0::2])

lista.append(56)
lista.append('two')

print(lista)

lista[0:3] = ["raz", "dwwa"]

print(lista)

# print("raz" in lista)

lista2 = lista

print(lista, lista2)


print(lista[0].count("raz"))