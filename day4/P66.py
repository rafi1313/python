class Zawodnik:
    def __init__(self, imie, wzrost, waga):
        self.imie = imie
        self.wzrost = wzrost
        self.waga = waga

    def bmi(self):
        return self.waga / (self.wzrost / 100) ** 2


tomek = Zawodnik("Tomek", 180, 185)

print(tomek.bmi())
