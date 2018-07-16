import pymysql


class Logowanie:

    def __init__(self):
        self.conn = pymysql.connect('localhost', 'root', 'SqlAccount!23', 'p80', charset='utf8')
        self.c = self.conn.cursor()
        print('połączenie ustanowione!')
        self.logIn()

    def logIn(self):
        login = input("Login: ")
        passwrd = input("Password: ")

        self.c.execute("SELECT * FROM logowanie where login=%s and haslo=%s", (login, passwrd))
        LogRes = self.c.fetchall()
        if (len(LogRes) == 1):
            print("zalogowano")
            self.menu(LogRes[0][5])
        else:
            print("błędne hasło")

    def menu(self,permissions):
        while(True):
            if permissions =='1':
                dec = input('P-pokaż, D-dodaj, U-usuń, Z-zmień uprawnienia, Q-wyjście: ').upper()



            else:
                dec = input('P-pokaż, Q-wyjście: ').upper()

            if(dec == 'P'):
                self.select(permissions)
            elif(dec == 'D' and permissions=='1'):
                self.insert()
            elif (dec == 'U' and permissions=='1'):
                self.delete(permissions)
            elif (dec == 'Z' and permissions=='1'):
                self.update(permissions)
            elif(dec == 'Q'):
                print('Koniec')
                self.conn.close()
                break
            else:
                print('Podałeś krzaki')

    def select(self, permissions):
        self.c.execute('SELECT * FROM logowanie')
        result = self.c.fetchall()
        i = 1
        if permissions=='1':
            print('|%20s|%20s|%20s|%20s|%20s|%20s' % (
                "id", "Imię", "Nazwisko", "login", "hasło", "uprawnienia"))
            for row in result:
                print('|%20i|%20s|%20s|%20s|%20s|%20s' % (i, row[1], row[2], row[3], row[4], row[5]))
                i += 1
        else:
            print('|%20s|%20s|%20s|%20s|%20s' % (
                "id", "Imię", "Nazwisko", "login", "uprawnienia"))
            for row in result:
                print('|%20i|%20s|%20s|%20s|%20s' % (i, row[1], row[2], row[3], row[5]))
                i += 1
    def insert(self):
        imie = input('Imię = ')
        nazwisko = input('Nazwisko = ')
        login = input('login = ')
        haslo = input('Hasło = ')
        uprawnienia = input('Uprawnienia = ')

        self.c.execute(
            'INSERT INTO logowanie ( imie, nazwisko, login, haslo, uprawnienia) VALUES (%s,%s,%s,%s,%s)',
            (imie, nazwisko, login, haslo, uprawnienia))

        dec = input('Na pewno dodać nowe dane ? T/N').upper()
        if (dec == 'T'):
            self.conn.commit()
            print('Dodano')
        else:
            self.conn.rollback()
            print('Anulowano operację')

    def delete(self,permissions):
        self.select(permissions)
        login = input('Podaj login osoby, którą zamierzasz usunąć = ')
        self.c.execute('DELETE FROM logowanie WHERE login=%s', login)
        dec = input('Na pewno usuwamy? T/N').upper()
        if (dec == 'T'):
            self.conn.commit()
            print('usunięto')
        else:
            self.conn.rollback()
            print('wracasz do gry')

    def update(self,permissions):
        self.select(permissions)
        login = input('Podaj login osoby, której zamierzasz zmodyfikować uprawnienia = ')
        value = input('Podaj nową wartość')

        # sql = ('UPDATE logowanie SET {}=%s WHERE login=%s').format(column)
        self.c.execute('UPDATE logowanie SET uprawnienia=%s WHERE login=%s', (value, login),)

        # self.c.execute('UPDATE pracownicy SET {1}=%s WHERE pesel=%s', (column, value, pesel))
        dec = input('Na pewno zmodyfikować dane ? T/N').upper()
        if (dec == 'T'):
            self.conn.commit()
            print('zmieniono')
        else:
            self.conn.rollback()
            print('wracasz do gry')

obj = Logowanie()