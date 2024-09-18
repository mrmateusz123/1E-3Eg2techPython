p1 = open("liczby1.txt")
l1 = list(map(int,p1.read().split()))
p2 = open("liczby2.txt")
l2 = list(map(int,p2.read().split()))


p1.close()
p2.close()
def z3():
    s=0
    for li in l1:
        s+=ldzwl(li)
    print(s)
def z4():
    endl = 0
    s=0
    ts=0
    for li in l2:
        s=0
        for i in range(1,li):
           if(li%i==0 and czyp(i)==True):
               s+=i
        if(s>ts):
            ts=s
            endl=li
    print(endl)
def  z5():
    scz=[]
    for li in l2:
        scz.append(sczp(li))
    mini = min(scz)
    for i in range(len(l2)):
        if(scz[i]==mini):
            print(i)
def z6():
    print()
def ldzwl(n):
    ile = 0
    for i in range(1,n):
        if(n%i==0):
            ile+=1
    return ile
def czyp(n):
    t = True
    for i in range(2,n):
        if n%i==0:
            t=False
    return t
def sczp(n):
    cz=2
    s=0
    while n>1:
        while n%cz==0:
            s+=cz
            n//=cz
        cz+=1
    return s

z4()
