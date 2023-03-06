# KOD HUFMANNA
W="ABCCCDDDDDEFGGGHHIJJ"
E="AB2C5DEF3G2HI2J"

H=""
l=1
for i in range(len(W)-1):
  if(W[i]==W[i+1]):
    l+=1
  else:
    if(l>1):
      H+=str(l)
    H+=W[i]
    l=1
if(l>1):
  H+=str(l)
  H+=W[i]
print(W)
print(H)



w="ABBCCCDDEFF"
h=""
l1=1
for i in range(len(w)-1):
  if(w[i]==w[i+1]):
    l1+=1
  else:
    if(l1>1):
      h+=str(l1)   
    h+=w[i]
    l1=1
if(l>1):
  h+=str(l)
  h+=w[i] 
print(w)
print(h)