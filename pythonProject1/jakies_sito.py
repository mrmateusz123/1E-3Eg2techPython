n = int(input())
czy_pier = [True]*(n+1)
p=2
while p*p<=n:
    if(czy_pier[p]):
        for i in range(p*p,n+1,p):
            czy_pier[i] = False
    p+=1
# for i in range(2, ile):
#     if (czy_pier[i] and (i + 1) % 2 == 0 or (i + 1) % 3 == 0):
#         czy_pier[i] = False
for i in range(n):
    print(i+1," ",czy_pier[i])
