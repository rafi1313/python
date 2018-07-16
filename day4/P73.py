
class Pracownicy:
    def __init__(self, imie, nazwisko, kontrakt, pensja):
        self.imie = imie
        self.nazwisko = nazwisko
        self.kontrakt = kontrakt
        self.pensja = pensja

    def __str__(self):
        return 'Imię i nazwisko: {} {} Kontrakt: {} Pensja: {} '.format(self.imie, self.nazwisko, self.kontrakt, self.pensja)

    def zmienKontrakt(self, pensja):
        self.kontrakt = "Etat"
        self.pensja = pensja


class Firma:
    def __init__(self, nazwa):
        self.nazwa = nazwa
        self.listaPracownikow = []

    def menu(self):

        while True:
            userInput = (input('Wybierz opcję: D-dodaj, P-pokaż, U- usuń, Z-zmiana kontraktu, Q-koniec ')).upper()
            if userInput == 'D':
                etatInput = input("Podaj typ pracownika: E-etat (domyślne)/S-staż ").upper()
                imie = input("Podaj imie pracownika: ")
                nazwisko = input("Podaj nazwisko pracownika: ")
                if etatInput == 'S':
                    etat = 'Staż'
                    pensja = 1000
                else:
                    etat = 'etat'
                    pensja = float(input("Podaj pensję pracownika: "))

                pracownik = Pracownicy(imie, nazwisko, etat, pensja)
                self.listaPracownikow.append(pracownik)

            elif userInput == 'P':
                for i in self.listaPracownikow:
                    print(i)
            elif userInput == 'U':
                userInput = int(input("Podaj id pracownika do usunięcia: "))
                self.listaPracownikow.pop(userInput)
            elif userInput == 'Z':
                userInput = int(input("Podaj id pracownika do zmiany kontraktu: "))
                nowaPensja = float(input("Podaj pensję pracownika: "))
                self.listaPracownikow[userInput].zmienKontrakt(nowaPensja)
            elif userInput == 'Q':
                break
            else:
                print('Niewłaściwa opcja.')


firma1 = Firma("Superb")
firma1.menu()
