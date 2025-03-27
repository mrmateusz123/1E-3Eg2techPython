def z1():
    bin = list(input("licz: ").split(','))
    wyn = 0
    pot = 1
    tak = 1
    for cz in bin:
        if tak == 1:
            cz = cz[::-1]
        for i in cz:
            if (i == "1"):
                wyn += 2 ** (pot - 1)
            pot+=tak
        tak = -1
        pot = 0
    print(wyn)


def z2():
    dec = list(input().split(","))
    bin = ""
    cz1 = int(dec[0])
    b2in = 0
    while cz1>0:
        bin+=str(cz1%2)
        cz1=cz1//2
    bin = bin[::-1]
    print(bin)
    pot = -1
    print("0."+dec[1])
    cz2 = int("0."+dec[1])
    while b2in != cz2:
        if b2in + 2**pot < cz2:
            b2in += 2**pot
        pot-=1
        print(b2in,int("0,",dec[1]))
    print(bin)


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
