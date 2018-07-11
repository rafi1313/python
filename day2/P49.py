konta = {'admin': 'admin', 'user': 'user'}

loginInput = input("Podaj login: ")
passInput = input("Podaj hasło: ")

if loginInput == 'admin' and konta[loginInput] == passInput:
    print("Panel administratora")
elif loginInput == 'user' and konta[loginInput] == passInput:
    print("Panel administratora")
else:
    print("Błąd logowania!\nNiepoprawny login lub/i hasło")
