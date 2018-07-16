def silnia(n):
    wynik = 1
    for i in range(1, n + 1):
        wynik *= i
    return wynik

#
# print(silnia(4))
# print(silnia(5))
# print(silnia(6))
# print(silnia(11))
print(silnia(90))
