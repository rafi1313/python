
def dodaj():
    imie = input("Podaj imię studenta: ")
    nazwisko = input("Podaj nazwisko studenta: ")
    grupa = int(input("Podaj grupę studenta: "))
    file = open('dane.txt',"a")
    file.write('%s,%s,%i\n' % (imie, nazwisko, grupa))
    file.close()


def pokaz():
    file = open('dane.txt', "r")

    # print(type(file))
    # print(file)
    for line in file:
        dane = line.strip().split(',')
        # print(dane)
        # print(type(dane))
        print('{:>10} {:>10} {:>10}'.format(dane[0],dane[1],dane[2]))
    # print(file.readline())

def usun():
    toDelete = input("Podaj nazwisko studenta do usunięcia: ")
    file = open('dane.txt', "r")
    listaStudentow = []
    liczbaUsuniec = 0
    for student in file:
        # print(type(student))
        dane = student.strip().split(',')
        # print(dane)
        if dane[1] != toDelete:
            listaStudentow.append(student)
        else:
            listaStudentow += 1
    file.close()
    # print(listaStudentow)
    file = open('dane.txt', "w")
    file.writelines(listaStudentow)
    file.close()
    if liczbaUsuniec == 0:
        print("Nie znaleziono studenta o tym nazwisku")
    else:
        print("Liczba usuniętych studentów o tym nazwisku: " + str(liczbaUsuniec))
while True:
    userInput = input("Podaj działanie do wykonania [D-dodaj, U-usuń, P-pokaż, Q-wyjście]: ").upper()

    if userInput == 'D':
        dodaj()

    elif userInput == "P":
        pokaz()
    elif userInput == "Q":
        break
    elif userInput == "U":
        usun()
    else:
        print("Niewłaściwa opcja")