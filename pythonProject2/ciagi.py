def z1():
    ciag = list(map(int,open("liczby.txt","r").readline().split()))
    for i in range(1,len(ciag)+1):
        for k in range(len(ciag)-i+1):
            print(*ciag[k:k+i])
        print()
def z2():
    ciag = list(map(int, open("liczby.txt", "r").readline().split()))
    for i in range(len(ciag)):
        for j in range(len(ciag)-i):
            print(*ciag[i:j+1+i])
        print()
def z3():
    ciag = list(map(int, open("liczby.txt", "r").readline().split()))
    for i in range(len(ciag)-4):
        print(*ciag[i:i+5],"suma:",sum(ciag[i:i+5]))
def z4():
    ciag = list(map(int, open("liczby.txt", "r").readline().split()))
    for i in range(len(ciag)-3):
        print(*ciag[i:])
def z5():
    pass
def z6():
    ciag = list(map(int, input().split(" ")))
    if(z610help(ciag),"<="): print("tak")
    else: print("nie")
def z610help(ciag,znak):
    for i in range(len(ciag)-1):
        if(exec("ciag[i]" + znak + "ciag[i+1])")):
            return False
    return True
def z7():
    pass
def zad():
    inp = input("Zadanie(q by zakończyć): ")
    if(inp != "q"):
        try:
            exec("z" + inp + "()")
            print('\n')
        except:
            print("błąd")
        zad()
print(exec("1<2"))
zad()
