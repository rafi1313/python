legenda = {"0": "zero", "1": "jeden", "2": "dwa", "3": "trzy", "4": "cztery", "5": "pięć", "6": "sześć", "7": "siedem",
           "8": "osiem", "9": "dziewięć"}

userInput = input("Wpisz cyfry do konwersji: ")
if userInput.isdigit():
    for index in list(userInput):
        print(legenda[index], end=' ')
else:
    print('To nie jest ciąg cyfr!')
