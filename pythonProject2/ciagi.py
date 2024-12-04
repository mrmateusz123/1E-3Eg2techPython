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
def z610help(znak):
    ciag = list(map(int, input().split(" ")))
    for i in range(len(ciag)-1):
        if(eval(f"{ciag[i]} {znak} {ciag[i+1]}")==False):
            return False
    return True
def z6():
    if(z610help("<")): print("tak")
    else: print("nie")

def z7():
    if(z610help(">")): print("tak")
    else: print("nie")

def z8():
    if (z610help(">=")):
        print("tak")
    else:
        print("nie")
def z9():
    if(z610help("<=")): print("tak")
    else: print("nie")
def z10():
    ciag = list(map(int, input().split(" ")))
    if(z610help("=")): print("tak")
    else: print("nie")
def z11():
    ciag = list(map(int,open("liczby.txt","r").readline().split()))
    najciag = []
    najciag2 = []
    for i in range(1,len(ciag)):
        if(ciag[i-1]<=ciag[i]):
            najciag.append(ciag[i-1])
        else:
            najciag.append(ciag[i-1])
            if(len(najciag)>=len(najciag2)):
                najciag2=najciag
            najciag = []
    print(len(najciag2))
def z12():
    ciag = list(map(int, open("liczby.txt", "r").readline().split()))
    najciag = []
    najciag2 = []
    for i in range(1, len(ciag)):
        if (ciag[i - 1] <= ciag[i]):
            najciag.append(ciag[i - 1])
        else:
            najciag.append(ciag[i - 1])
            if (len(najciag) > len(najciag2)):
                najciag2 = najciag
            najciag = []
    print(najciag2)
def z13():
    pliczek = list(map(int,open('pi.txt').read().split()))
    pliczekz = open("pi_przykład.txt",'w')
    t=0
    for i in range(len(pliczek)-1):
        if((pliczek[i]*10)+pliczek[i+1]>90):
            t+=1
            print(i+1,pliczek[i],pliczek[i+1])
    print("t=",t)
    pliczekz.write(f'{t}')
    pliczekz.close()
def z14():
    pliczek = list(map(int,open('pi.txt').read().split()))
    pliczekz = open("pi_przykład.txt",'w')
    test = []
    for i in range(10):
        for j in range(10):
            test.append(str(i)+str(j))
    naj = 0
    najm = 0
    najmm = 0
    for i in range(len(test)):
        for j in range(len(pliczek)-1):
            if(test[i]==f'{str(pliczek[j])}{str(pliczek[j+1])}'):
                naj+=1
                print(test[i],pliczek[j],pliczek[j+1])
        if(naj>najm):
            najm = naj
            najmm = test[i]
    print(najmm)



def zad():
    inp = input("Zadanie(q by zakończyć): ")
    if(inp != "q"):
        try:
            exec("z" + inp + "()")
            print('\n')
        except Exception as error:
            print("błąd:",error)
        zad()
zad()
