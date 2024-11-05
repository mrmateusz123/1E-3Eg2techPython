import random


def scal(T,left,srodek,right,pom):
    i = left
    j = srodek+1
    k = left
    while i <=srodek and j<=right:
        if T[i] < T[j]:
            pom[k] = T[i]
            i+= 1
        else:
            pom[k] = T[j]
            j+=1
        k+=1

    while i<= srodek:
        pom[k] = T[i]
        i+=1
        k+=1
    while j <= right:
        pom[k] = T[j]
        j += 1
        k += 1

    for i in range(left,right+1):
        T[i] = pom[i]


def sortuj(T,left,right,pom):
    if left< right:
        middle = (left+right)//2
        sortuj(T,left,middle,pom)
        sortuj(T,middle+1,right,pom)
        scal(T,left,middle,right,pom)
def zad1():
    T = [int(i) for i in input("wpisz liczby: ").split()]
    pom = [0 for i in range(len(T))]
    print(T)
    sortuj(T, 0, len(T) - 1,pom)
    print(T)
def zad2():
    plik = open("ciagi.txt","r")
    plik2 = open("winiki_2.txt","w")
    ciag = list(map(int,plik.read().split()))
    pom = [0 for i in range(len(ciag))]
    sortuj(ciag, 0, len(ciag) - 1,pom)
    for i in ciag:
        plik2.write(str(i) + " ")
def zad3():
    plik = open("wyniki_3.txt","w")
    ciag = [random.randint(1,1000000) for i in range(1000000)]
    pom = [0 for i in range(len(ciag))]
    sortuj(ciag, 0, len(ciag) - 1,pom)
    for i in ciag:
        plik.write(str(i) + " ")
def zadania():
    n = input("zadanie: ")
    if n!='q':
        if(n=='1'):
            zad1()
        elif(n=='2'):
            zad2()
        elif n=='3':
            zad3()
        else:
            print("błąd")
        print("\n\n")
        zadania()
    else:
        print("end")
zadania()