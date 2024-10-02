def wy(T,a,n):
    lewy = 0
    prawy =  n - 1
    while lewy < prawy:
        srodek = (lewy+prawy)//2
        if T[srodek] < a:
            lewy = srodek + 1
        else:
            prawy = srodek
    if(T[lewy]==a):
        return True
    return False

def so(LI):
    for i in range(len(LI)-1):
        if(LI[i]>LI[i+1]):
            return False
    return True

def z1():
    L = []
    for i in range(10):
        L.append(int(input()))
    if(so(L)==False):
        print("ciąg musi być uporządkowany niemalejąco")
        z1()
    a = int(input("Podaj a: "))
    if(wy(L,a,len(L))):
        print("tak")
    else:
        print("nie")
def z2():
    L = []
    for i in range(10):
        L.append(int(input()))
    if(so(L)==False):
        print("ciąg musi być uporządkowany niemalejąco")
        z1()
    a = int(input("Podaj a: "))
    if(wy(L,a,len(L))):
        print("tak")
    else:
        print("nie")


def zadania():
    zad = int(input("które zadanie?:"))
    if (zad == 0):
        print("end")
    else:
        if zad == 1:
            z1()
            print()
        elif zad == 2:
            z2()
            print()
        zadania()

zadania()
