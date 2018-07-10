a = int(input("Wartosc calkowita: "))
b = float(input("Wartosc rzeczywista: "))
c = bool(int(input("Wartosc logiczna (Prawda[1]/Falsz[0]):")))
d = input("Wartosc tekstowa: ")
wynik = b * 10
print(wynik)
wynik = wynik **a
print(wynik)
wynik *= float(c)
print(wynik)
print(("podano napis: " + d + ', oraz obliczono ' + str(wynik) + '\n')*10)