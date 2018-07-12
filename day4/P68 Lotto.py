from random import randint


class Lotto:

    def __init__(self):
        self.wylosowane = set()

    def losowanie(self):
        while len(self.wylosowane) < 6:
            self.wylosowane.add(randint(0, 49))
        # print(sorted(self.wylosowane, reverse=True))
        self.wylosowane = list(self.wylosowane)
        print(type(self.wylosowane))
        (self.wylosowane).sort()
        # pom.sort()
        print(self.wylosowane)


losowanieLotto = Lotto()
losowanieLotto.losowanie()
