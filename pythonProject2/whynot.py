import random
def z1():
    pliczek = open('czemunie.txt','w')
    tak = []
    for i in range(1000000):
        print(i/1000000 * 100,"%")
        tak.append( random.randint(1,1000000))
        pliczek.write(str(tak[i]) + '\n')
    print("100%")
def z2():
    wsp = list(map(int, input("Podaj ciąg znaków: ").split()))
    x = int(input("Podaj x: "))
    n = len(wsp)
    stopien = n - 1
    w = wsp[n-1]
    for i in range(n-2,-1,-1):
        w = w*x+wsp[i]
    print(w)

def z4():
    pliczek = list(map(int,open('liczby (1).txt').read().split()))
    print(pliczek)
    dl = 1
    maxdl = dl
    for i in (0,len(pliczek)-1):
        print(pliczek[i])
        print(pliczek[i+1])
        print(i)
        print(len(pliczek)-1)
        if pliczek[i] < pliczek[i+1]:
            dl+=1
        else:
            if dl > maxdl:
                maxdl = dl
                dl = 1
    print(maxdl)
def z5():
    pliczek = list(map(int, open('ciag.txt').read().split()))
    maxs = 0
    t = []
    for i in range(0,len(pliczek)-2):
        if(sum(pliczek[i:i+3]) >= maxs):
            maxs = sum(pliczek[i:i+3])
            t = pliczek[i:i+3]
    print(maxs,t)
def z6():
    pliczek = list(map(int, open('ciag.txt').read().split()))
    pliczekniepliczek = [5,23,6,2,4,5,3,3]
    s = pliczek[0]
    maxs = 0
    t = []
    for i in range(len(pliczek)):
        for j in range(1,len(pliczek)-i+1):
            print(pliczek[i:i+j])
            s = sum(pliczek[i:i+j])
            if (s >= maxs):
                maxs = s
                t = pliczek[i:i+j]
            s = 0
    print(maxs,t)

def zad():
    inp = input("Zadanie(q by zakończyć): ")
    if (inp != 'q'):
        try:
            exec("z" + inp + "()")
            print('\n')
        except Exception as error:
            print("błąd:", error)
        zad()
zad()
