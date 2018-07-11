# licznik =10
# wartosc = 150
#
# while licznik<=wartosc:
#     licznik +=1
#     print("Jestem w pętli while.")

lista = [1, 56, 87, 146, 98, 1538, 516, 351, 3518, 864, 8186]

suma = 0

for q in lista:
    suma += q

srednia = suma / len(lista)
print(srednia)
