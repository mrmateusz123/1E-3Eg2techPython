pliczek = list(map(int, open('ciag.txt').readline().split()))
def z1():
    print()
def z2():
    print(pliczek)
    s = 0
    ms = 0
    ii = []
    iim = []
    for i in range(0,len(pliczek)-2):
        s+=pliczek[i] + pliczek[i+1] + pliczek[i+2]
        ii = [pliczek[i:i+3]]
        if(s>ms):
            ms = s
            iim = ii
        s = 0
        ii = []
    print(iim,ms)
def z3():
    s = 0
    ms = 0
    for i in range(len(pliczek)):
        for k in range(len(pliczek)-i):
            for j in range(0,i+1):
                print(pliczek[k+j],end=' ')
                s += pliczek[k+j]
            print(f's = {s}')
            if(s>ms):
                ms=s
            s = 0
            print()
        print()
    print(ms)

def z4():
    print()
def zad():
    inp = input("Zadanie(q by zakończyć): ")
    if (inp != "q"):
        try:
            exec("z" + inp + "()")
            print('\n')
        except Exception as error:
            print("błąd:", error)
        zad()
zad()
