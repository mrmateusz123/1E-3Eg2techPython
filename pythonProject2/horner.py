def horner(T,x,n):
    y = T[0]
    pot = 1
    for i in range(1,n):
        pot = pot * x
        y = y + T[i] * pot
    return y
def honer2(T,x,n):
    y =  T[n-1]
    for i in range(n-1,0,-1):
        y = x * y + T[i]
    return y
def z1():
    t = [int(i) for i in input().split()]
    x = int(input())
    print(honer2(t,x,len(t)))
    t.reverse()
    print(horner(t,x,len(t)))

z1()
