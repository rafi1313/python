import pymysql

class Pracownicy:
    def __init__(self):
        #try:
            self.conn = pymysql.connect('localhost', 'root', 'SqlAccount!23', 'baza_python_test', charset='utf8')
            self.c = self.conn.cursor()
            print('połączenie ustanowione!')
            self.menu()
        #except:
         #   print('błędne dane logowania!')

    def menu(self):
        while(True):

            dec = input('S-shows, I-insert, D-delete, U-upadete,  Q-Exit').upper()

            if(dec == 'S'):
                self.select()
            elif(dec == 'I'):
                self.insert()
            elif (dec == 'D'):
                self.delete()
            elif (dec == 'U'):
                self.update()
            elif(dec == 'Q'):
                print('Koniec')
                self.conn.close()
                break
            else:
                print('Podałeś krzaki')
    def select(self):
        self.c.execute('SELECT * FROM pracownicy')
        Result = self.c.fetchall()
        i=1
        print('|%20s|%20s|%20s|%20s|%20s|%20s|%20s' % ("Lp", "Imię", "Nazwisko", "Rok urodzenia", "Pensja", "Pesel", "Data zatrudnienia"))

        for row in Result:
            print('|%20i|%20s|%20s|%20s|%20s|%20s|%20s' % (i, row[1], row[2], row[3], row[4], row[5], row[6]))
            i+=1
    def insert(self):
        imie = input('Imię = ')
        nazwisko = input('Nazwisko = ')
        rokUrodzenia = int(input('Rok urodzenia = '))
        pensja = input('Pensja = ')
        pesel = input('Pesel = ')
        dataZatrudnienia = input('Data zatrudnienia (rrrr-mm-dd) = ')

        #try:
        self.c.execute('INSERT INTO pracownicy (imie, nazwisko, rokUrodzenia, pensja, pesel, dataZatrudnienia) VALUES (%s,%s,%s,%s,%s,%s)', (imie, nazwisko, rokUrodzenia, pensja, pesel, dataZatrudnienia))
        # except pymysql.InternalError as error:
        #    print("%s" % error)

        dec = input('Na pewno dodać nowe dane ? T/N').upper()
        if (dec == 'T'):
            self.conn.commit()
            print('dodano')
        else:
            self.conn.rollback()
            print('anulowano operację')

        #self.conn.commit()
    def delete(self):
        self.select()
        pesel = input('Podaj pesel osoby, którą zamierzasz usunąć = ')
        self.c.execute('DELETE FROM pracownicy WHERE pesel=%s', pesel)
        dec = input('Na pewno usuwamy? T/N').upper()
        if(dec == 'T'):
            self.conn.commit()
            print('usunięto')
        else:
            self.conn.rollback()
            print('wracasz do gry')
    def update(self):
        self.select()
        pesel = input('Podaj pesel osoby, którą zamierzasz modyfikować = ')
        column = input('Którą kolumnę chcesz edytować? ')
        value = input('Podaj nową wartość')

        sql = ('UPDATE pracownicy SET {}=%s WHERE pesel=%s').format(column)
        self.c.execute(sql, (value, pesel))

        #self.c.execute('UPDATE pracownicy SET {1}=%s WHERE pesel=%s', (column, value, pesel))
        dec = input('Na pewno zmodyfikować dane ? T/N').upper()
        if (dec == 'T'):
            self.conn.commit()
            print('zmieniono')
        else:
            self.conn.rollback()
            print('wracasz do gry')
obj = Pracownicy()