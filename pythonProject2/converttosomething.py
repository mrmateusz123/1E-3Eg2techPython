def z1():
    bin = list(input().split(','))
    wyn = 0
    pot = 1
    tak = 1
    for cz in bin:
        if tak == 1:
            cz = cz[::-1]
        for i in cz:
            if (i == "1"):
                wyn += 2 ** (pot - 1)
            pot += tak
        tak = -1
        pot = 0
    print(wyn)


def z2():
    dec = list(input().split(","))
    bin = ""


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
