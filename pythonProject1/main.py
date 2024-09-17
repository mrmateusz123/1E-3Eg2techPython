def czyP(n):
    for i in range(1,n):
        if(n%i!=0):
            return False
    return True


file = open('liczby1.txt','r')
file2 = open('liczby2.txt','r')
T=list(map(int,file.read().split()))
T2=list(map(int,file2.read().split()))
S = 0
for L in T:
    if(czyP(L)):
        S+=1
print(S)



file.close()