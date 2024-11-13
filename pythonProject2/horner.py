def horner(T,x,n):
    y = T[n]
    pot = 1
    for i in range(n,0,-1):
        pot = pot * x
        y += T[i-1] * pot
    return y
def honer2(T,x):
    n = len(T)-1
    if(n==0): return T[0]
    return x*honer2(T[1:],x)+T[0]

def z1():
    t = [int(i) for i in input().split()]
    x = t.pop(0)
    print(horner(t,x,len(t)-1))
def z2():
    t = [int(i) for i in input().split()]
    x = t.pop(0)
    print(honer2(t,x))
z2()
