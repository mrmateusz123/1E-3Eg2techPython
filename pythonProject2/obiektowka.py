class Prostokat:
    def __init__(self,dlugosc,szerokosc):
        self.a=dlugosc
        self.b=szerokosc
    def pole(self):
        return self.a*self.b
    def obwod(self):
        return self.a*2+self.b*2
class ProstokatExtra(Prostokat):
    def __init__(self,x,y):
        super().__init__(x,y)
    def wyswietl_pole(self):
        print(self.pole())
    def wyswietl_obwod(self):
        print(self.obwod())
class Osoba:
    def __init__(self,imie,nazwisko,wzrost,waga):
        self.imie = imie
        self.nazwisko = nazwisko
        self.wzrost = wzrost
        self.waga = waga
    def powitanie(self):
        print("Witaj",self.imie,self.nazwisko)
    def informacje(self):
        print(self.imie,self.nazwisko,self.waga,self.wzrost)
class Trojkat:
    def __init__(self,a,b,c,wysokosc):
        self.a = a
        self.b = b
        self.c = c
        self.wys = wysokosc
    def Pole(self):
        return (self.a * self.wys)/2
    def Obwod(self):
        return self.a + self.b + self.c
class kolo:
    def __init__(self,r):
        self.r = r
    def pole(self):
        return 3.141 * self.r**2
    def obwod(self):
        return 3.141 * self.r * 2
# l1 = int(input())
# l2 = int(input())
# prostokat1 = ProstokatExtra(l1,l2)
# prostokat1.wyswietl_pole()
# prostokat1.wyswietl_obwod()
# osoba1 = Osoba("Denys","Perehodko","140cm","200kg")
# osoba1.informacje()
# l1 = int(input())
# l2 = int(input())
# l3 = int(input())
# wys = int(input())
# tr1 =  Trojkat(l1,l2,l3,wys)
# print(tr1.Pole())
kolo1 = kolo(5)
print(kolo1.pole())
print(kolo1.obwod())
