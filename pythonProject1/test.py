def z1():
    n = int(input("podaj liczbe:"))
    if(n%2==0):print("TAK")
    else: print("nie")
    zada()
def z2():
    n = int(input("podaj liczbe:"))
    for i in range(1,n+1):
        if(n%i==0):
            print(i)
    zada()
def z3():
    suma = 0
    n = int(input("podaj liczbe:"))
    for i in range(1,n+1):
        if(n%i==0):
            suma+=i
    print(suma)
    zada()
def z4():
    suma = 0
    n = int(input("podaj liczbe:"))
    for i in range(1,n):
        if(n%i==0):
            suma+=1
    print(suma)
    zada()
def z5():
    T = True
    n = int(input("podaj liczbe:"))
    for i in range(2,n+1):
        if(n%i==0):
            for j in range(2,i):
                if(i%j==0):
                    T = False
            if(T==True):
                print(i)
            T=True
    zada()

def z6():
    a = int(input(": "))
    b = int(input(": "))
    s=0
    for i in range(1,a):
        if(a%i==0):
            s+=1
    for i in range(1,b):
        if(b%i==0):
            s+=1
    if(s==2):
       if(b-2==a or a-2==b):print("TAK")
       else: print("nie")
    else: print("nie")
    zada()
def z7():
    suma=0
    n= int(input("liczba:"))
    for i in range(1,n):
        if(n%i==0):
            suma+=i
    if(suma==n):
        print("TAK")
    else:
        print("NIE")
    zada()
def z8():
    a = int(input())
    b = int(input())
    sa = 0
    sb = 0
    for i in range(1,a):
        if(a%i==0):
            sa+=i
    for i in range(1,b):
        if(b%i==0):
            sb+=i
    if(sa==b and sb==a):
        print("Tak")
    else:
        print("Nie")
    zada()
def z9():
    n=int(input("n:"))
    c=2
    while(n>1):
        while(n%c==0):
            print(n," ",c)
            n=n/c
        c+=1
def z10():
    n=int(input("n:"))
    c=2
    s=0
    while(n>1):
        while(n%c==0):
            s+=c
            n=n/c
        c+=1
    print(s)
def z11():
    n=int(input("n:"))
    c=2
    s=0
    while(n>1):
        while(n%c==0):
            s+=c
            n=n/c
        c+=1
    for i in range(1,s):
        if(s%i==0):
            c += 0
        else:
            c += 1
    if(c==0):
        print("tak",s)
    else:
        print("nie",s)
def z12():
    n=int(input("n:"))
    c=2
    list = []
    s=0
    while(n>1):
        while(n%c==0):

            for i in range(0,len(list)):
                if(c!=list[i]):

                    s+=1
            n=n/c
        c+=1
    print(s)
def z13():
    n=int(input("n:"))
    n2=str(n)
    l=[]
    t=0
    print(len(n2))
    while(n>0):
        l[t]=n[(len(n2)-t-1)]
        t+=1
    for i in range(len(l)):
        print(l[i])
    c=2
    while(n>1):
        while(n%c==0):
            n=n/c
        c+=1
def zada():
    zad = int(input("które zadanie?"))
    if(zad==1): z1()
    elif(zad==2): z2()
    elif(zad==3): z3()
    elif(zad==4): z4()
    elif(zad==5): z5()
    elif(zad==6): z6()
    elif(zad==7): z7()
    elif(zad==8): z8()
    elif(zad==9): z9()
    elif(zad==10): z10()
    elif(zad==11): z11()
    elif(zad==12): z12()
    elif(zad==13): z13()
    elif(zad==0): print("end")
    else:
        print("ni ma takiego zadania")
        zada()
zada()
