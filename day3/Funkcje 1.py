# def srednia(x, y, z):
#     wynik = (x + y + z) / 3
#     return wynik
#
#
# x = srednia(2, 3, 5)
# print(x)


# def potega(n, w):
#     return n ** w
#
#
# print(potega(3, 10))
#
#
# def powitanie(imie):
#     print("Hello " + imie)
#
#
# powitanie("Kot")
#
# print(type(divmod(7, 3)))
#
#
# def test(a, b=5):
#     print(a, b)
#
#
# test(73)


def srednia(*args):
    if len(args)==0:
        return 0
    else:
        sum = 0
        for x in args:
         sum += x
        return sum / len(args)

print(srednia())

print(srednia(1, 3, 4, 6,7))
