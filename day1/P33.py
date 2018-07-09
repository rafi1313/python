SPK = float(input("Stan początkowy konta: "))
P = float(input("Stopa oprocentowania w %: "))
N = float(input("Liczba lat: "))

stanKonta = round(((1+P/100)**N)*SPK, 2)
print("Ostateczny stan konta:" + str(stanKonta))