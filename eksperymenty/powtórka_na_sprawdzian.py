def z1():
    bin = input().split(".")
    sys = int(input())
    pot = 0
    wyn = 0
    pliczek = open("test.txt","w")
    for i in bin:
        if(pot == 0):
            i=i[::-1]
        for j in i:
            wyn+=(int(j)*(sys**pot))
            pot+=1
        pot = -1
    pliczek.write(str(wyn))
    pliczek.close()
    print(wyn)
def z2():
    pliczek = open("test2.txt","r")
    for i in pliczek:
        t = i.split(".")
        print(t)
    pliczek.close()

def zad():
    inp = input("Zadanie(q by zakończyć,t by bardziej przetestować): ")
    if (inp != 'q'):
        try:
            if (inp != 't'):
                exec("z" + inp + "()")
            else:
                inp = input("testowanie: ")
                if (inp != 'q'):
                    exec(inp)
            print('\n')
        except Exception as error:
            print("błąd:", error)
        zad()


zad()