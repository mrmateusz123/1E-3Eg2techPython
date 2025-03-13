import random

def zp1(t):
    n = len(t)
    mi = 0
    ma = 0
    if(t[0]<t[1]):
        mi = t[0]
        ma = t[1]
    else:
        mi = t[1]
        ma = t[0]
    for i in range(2,n-1,2):
        if t[i]<t[i+1]:
            if t[i]<mi:
                mi = t[i]
            if t[i+1] > ma:
                ma = t[i+1]
        else:
            if t[i+1]<mi:
                mi = t[i+1]
            if t[i] > ma:
                ma = t[i]
    print(t,mi,ma)
    return mi, ma
def z1():
    t = [random.randint(1,1000) for i in range(100)]
    mi = ma = t[0]
    for i in t:
        if i >= ma:
            ma = i
        if i <= mi:
            mi = i
    print(t)
    print(mi,ma)
def z2():
    print("3/2n - 2")
    t = [random.randint(1,1000) for i in range(100)]
    print(len(t)*3/2-2)
def z3():
    t = [random.randint(1,1000) for i in range(100)]
    zp1(t)
    print(len(t)*3/2-2)
def z4():
    t = [random.randint(1, 1000) for i in range(11)]
    n = len(t)
    mi = 0
    ma = 0
    if (t[0] < t[1]):
        mi = t[0]
        ma = t[1]
    else:
        mi = t[1]
        ma = t[0]
    for i in range(2, n - 1, 2):
        if t[i] < t[i + 1]:
            if t[i] < mi:
                mi = t[i]
            if t[i + 1] > ma:
                ma = t[i + 1]
        else:
            if t[i + 1] < mi:
                mi = t[i + 1]
            if t[i] > ma:
                ma = t[i]
    print(t, mi, ma)
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
