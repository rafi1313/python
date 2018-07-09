# import os
import time
import winsound

czasOdliczany = int(input("Podaj czas do odliczenia w sekundach:"))
freaquency = 1500
duration = 500


def beepfunction():
    for x in range(0, 3):
        winsound.Beep(freaquency, duration)
        time.sleep(1)


def countdown(t):
    while t:
        mins, secs = divmod(t, 60)
        timeformat = '{:02d}:{:02d}'.format(mins, secs)
        print(timeformat, end='\r')
        time.sleep(1)
        t -= 1
    print('Goodbye!\n\n\n\n')
    beepfunction()


countdown(czasOdliczany)