def srednia(*args):
    if len(args) == 0:
        return 0
    else:
        suma = 0
        for x in args:
            suma += x
        return suma / len(args)


print(srednia())

print(srednia(1, 3, 4, 6, 7))
print(srednia(4, 5, 3, 3, 2, 1))
