
def z1():
    pliczek = list(map(int,open('pi.txt').read().split()))
    pliczekz = open("pi_przykład.txt",'w')
    t=0
    for i in range(len(pliczek)-1):
        if((pliczek[i]*10)+pliczek[i+1]>90):
            t+=1
            print(i+1,pliczek[i],pliczek[i+1])
    print("t=",t)
    pliczekz.write(f'{t}')
    pliczekz.close()
def z2():
    pliczek = list(map(int,open('pi.txt').read().split()))
    pliczekz = open("pi_przykład.txt",'w')
    test = []
    for i in range(10):
        for j in range(10):
            test.append(str(i)+str(j))
    naj = 0
    najm = 0
    najmm = 0
    for i in range(len(test)):
        for j in range(len(pliczek)-1):
            if(test[i]==f'{str(pliczek[j])}{str(pliczek[j+1])}'):
                naj+=1
                print(test[i],pliczek[j],pliczek[j+1])
        if(naj>najm):
            najm = naj
            najmm = test[i]
    print(najmm)
def z3():
    pliczek = list(map(int,open("pi_przyklad.txt").read().split()))
    odp = ""
    odpli = 0
    for i in range(1,len(pliczek)-6):
        if(pliczek[i]<=pliczek[i+1] and pliczek[i+1]<=pliczek[i+2] and pliczek[i+3]>=pliczek[i+4] and pliczek[i+4]>=pliczek[i+5]):
            odp += f"{pliczek[i]} {pliczek[i+1]} {pliczek[i+2]} {pliczek[i+3]} {pliczek[i+4]} {pliczek[i+5]} i:{i+1}-{i+6}\n"
            odpli += 1
    print(odp , odpli)
def z4():
    pliczek = list(map(int,open("pi_przyklad.txt").read().split()))
    odp = f"{pliczek[0]}"
    odpmax = f"{pliczek[0]}"
    odpli = 1
    odplimax = 1
    test = True
    for i in range(1,len(pliczek)):
        if int(odp(len(odp)-1)) < pliczek[i] and test == True:
            odp += str(pliczek[i])
            odpli += 1
        elif int(odp(len(odp)-1)) > pliczek[i] and test == True:
            odp += str(pliczek[i])
            odpli += 1
            test = False
        elif int(odp(len(odp)-1)) < pliczek[i] and test == False:
            
        elif int(odp(len(odp)-1)) > pliczek[i] and test == False:
            
def zad():
    inp = input("Zadanie(q by zakończyć): ")
    if(inp != "q"):
        try:
            exec("z" + inp + "()")
            print('\n')
        except Exception as error:
            print("błąd:",error)
        zad()
zad()