import random
def z1():
    imie = input()
    nazwisko = input()
    plik = open("daneosobowe.txt","w")
    plik.write(imie + "\n" + nazwisko)
    plik.close()
def z2():
    z1()
    plik = open("daneosobowe.txt","r")
    print("witaj",end=" ")
    for l in plik:
        l = l.strip()
        print(l,end=" ")
    print()
def z3():
    plik = open("losowe.txt","w")
    for i in range(10):
        plik.write(str(random.randint(1, 100)) + "\n")
    plik.close()
    plik = open("losowe.txt","r")
    suma = 0
    max = 0
    min = 100
    sr = 0
    for l in plik:
        l = int(l.strip())
        suma += l
        if l > max:
            max = l
        if l < min:
            min = l
        sr+=1
    print("suma: ",suma," max: ",max," min: ",min," srednia: ", suma/sr)
def z4():
    plik = open("ciagi.txt","r")
    lci = int(plik.readline().rstrip())
    for i in range(lci-1):
        linia = plik.readline().rstrip().split()
        dl = int(linia[0])
        ciag = list(map(int,(linia[1:])))




def zadania():
    n = int(input("które zadanie: "))
    if(n==1):
        z1()
        zadania()
    elif(n==2):
        z2()
        zadania()
    elif n==3:
        z3()
        zadania()
    elif n==4:
        z4()
        zadania()
    elif n==0:
        print("end")
    else:
        print("błąd")
        zadania()

zadania()
