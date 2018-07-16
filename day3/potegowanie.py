
podstawa = float(input("Podaj podstawę do potęgowania: "))
wykladnik = int(input("Podaj wykładnik do potęgi: "))
wynik = 1
for index in range(0,wykladnik):
    wynik = podstawa * wynik

print("Wynikiem potęgowania jest: " + str(wynik))