phoneBook = []


while (True):
    print("d-Dodaj, P-pokaż, Q-wyjście")

    dec = input("Podaj co robimy?: ")
    dec = dec.upper()
    if dec =="D":
        imie = input("Podaj imię: ")
        nazwisko = input("Podaj nazwisko: ")
        nrTel = input("Podaj numer telefonu: ")
        kontakt = []
        kontakt.append(imie)
        kontakt.append(nazwisko)
        kontakt.append(nrTel)
        phoneBook.append(kontakt)


    if dec =="Q":
        break

    if dec =="P":
        for ind, index in enumerate(phoneBook):
            print(ind, '=>',index[0] + ' '+ index[1]+': '+index[2])
            # print(phoneBook[index])
            # print( index[1])