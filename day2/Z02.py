chleb = 6.50
sok = 4
paczek = 5.5

liczbaChleb = int(input("Liczba chlebów do zakupienia: "))
liczbaSok = int(input("Liczba soków do zakupienia: "))
liczbaPaczek = int(input("Liczba pączków do zakupienia: "))

print("Podsumowanie zakupów:")
print("Liczba zakupionych chlebów: " + str(liczbaChleb) + 'szt. o wartości ' + str(liczbaChleb * chleb))
print("Liczba zakupionych soków: " + str(liczbaSok) + 'szt. o wartości ' + str(liczbaSok * sok))
print("Liczba zakupionych pączków: " + str(liczbaPaczek) + 'szt. o wartości ' + str(liczbaPaczek * paczek))

print("Łączna wartośc zakupów: " + str(liczbaChleb * chleb + liczbaSok * sok + liczbaPaczek * paczek))

