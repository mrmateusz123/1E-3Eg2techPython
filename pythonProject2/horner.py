def horner(T,x,n):
    y = T[n]
    pot = 1
    for i in range(n,0,-1):
        pot = pot * x
        y += T[i-1] * pot
    return y
def honer2(T,x):
    n = len(T)-1
    if(n==0): return T[n]
    return x*honer2(T[:n],x)+T[n]

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
def z6():
    t = [int(i) for i in input()]
    x = 2
    print(honer2(t,x))
def z7():
    t = [int(i) for i in input()]
    p = int(input())
    print(honer2(t,p))
print(exec(input()+"()"))
