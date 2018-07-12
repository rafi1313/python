class Dziekanat:

    def __init__(self):
        self.studenci = []

    def dodajStudenta(self, nrIndeksu, imie, nazwisko):
        self.studenci.append([nrIndeksu, imie, nazwisko])

    def listaStudentow(self):
        for i in self.studenci:
            print('Nr indeksu: {:s} | Imię i nazwisko studenta: {} {}'.format(i[0], i[1], i[2]))
        print('\n')

    def usunStudenta(self, nrIndeksu):
        for i, dane in enumerate(self.studenci):
            if dane[0] == nrIndeksu:
                self.studenci.pop(i)


dziekanat1 = Dziekanat()
dziekanat1.dodajStudenta("211478", 'Jan', "Kowal")
dziekanat1.dodajStudenta("218678", 'Adam', "Kula")
dziekanat1.dodajStudenta("211748", 'Marek', "Mapa")
dziekanat1.listaStudentow()
dziekanat1.usunStudenta('218678')
dziekanat1.listaStudentow()
