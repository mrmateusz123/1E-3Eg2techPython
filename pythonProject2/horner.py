def horner(T,x,n):
    y = T[n]
    pot = 1
    for i in range(n,0,-1):
        pot = pot * x
        y += T[i-1] * pot
    return y
def honer2(T,x):
    n = 0
    if(n==len(T)-1): return T[len(T)-1]
    return x*honer2(T[:len(T)-1],x)+T[len(T)-1]

def z1():
    t = [int(i) for i in input().split()]
    x = t.pop(0)
    print(horner(t,x,len(t)-1))
def z2():
    t = [int(i) for i in input().split()]
    x = t.pop(0)
    print(honer2(t,x))
def z5():
    t = [int(i) for i in input().split()]
    x = t.pop(0)
    t.reverse()
    print(horner(t,x,len(t)-1))
for i in range(1,3):
    print(exec(f"z{str(i)}()"))
