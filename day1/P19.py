imie = 'Adam'
nazwisko = 'Kowalski'
wiek = 45
stanowisko = 'mlodszy inżunier procesu'
pensjaBrutto = 6000
plec = "Pan"

napis = plec + ' ' + imie + ' ' + nazwisko + ' ' + '(wiek:' + str(wiek) + 'lat)\npracuje na stanowisku ' + stanowisko
napisCz2 = '\n(pensja:' + str(pensjaBrutto) + ' brutto)\n'
napis = napis + napisCz2
print(napis*10)

import winsound
import time

freaquency = 500
duration = 1000
winsound.Beep(freaquency, duration)

soundRange = 5
for x in range(0,5):
    winsound.Beep(freaquency, duration)
    time.sleep(1)