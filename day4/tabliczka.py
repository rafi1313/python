def tabliczka(rows, columns):
    print("Tabliczka mnożenia\n")
    print("-\t" * columns)
    for x in range(1, rows + 1):

        for y in range(1, columns + 1):
            if y == columns:
                print('{:d}'.format(x * y), end="\n")
            else:
                print('{:d}'.format(x * y), end="\t")


tabliczka(18, 25)


import math

math.sin(45)