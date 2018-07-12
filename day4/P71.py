class Produkt:
    def __init__(self, nazwa, cena):
        self.nazwa = nazwa
        self.cena = cena

    def __str__(self):
        return 'Nazwa produktu: {}; Cena produktu: {}'.format(self.nazwa, self.cena)


class Oprogramowanie(Produkt):
    def __init__(self, nazwa, cena, jezyk, system):
        super().__init__(nazwa, cena)
        self.jezyk = jezyk
        self.system = system

    def __str__(self):
        return super().__str__() + '\nJęzyk: {} | System: {}'.format(self.jezyk, self.system)
        # 'Nazwa produktu: {}; Cena produktu: {}\nJęzyk: {}'.format(self.nazwa, self.cena, self.jezyk)


class Szkolenia(Oprogramowanie):
    def __init__(self, nazwa, cena, jezyk, system, termin):
        super().__init__(nazwa, cena, jezyk, system)
        self.termin = termin

    def __str__(self):
        return super().__str__() + '\nTermin: {}'.format(self.termin)


produkt1 = Produkt('Back-End Developer', '123456')
print(produkt1)

print('\n')
windows1 = Oprogramowanie("Windows", '159', 'ENG', 'XP', )
print(windows1)

print('\n')

kurs = Szkolenia('Back-End Developer', '456', 'Java', 'Windows', '2018.07.01')
print(kurs)
