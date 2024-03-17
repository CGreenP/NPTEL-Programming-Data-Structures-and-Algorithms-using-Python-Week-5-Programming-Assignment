x=[]
def bre1(x):
    l=len(x)
    inp=""
    count=0
    for i in range(l):
        count+=1
        if(x[i]=="~"):
            break
        else:
            inp+=x[i]
    return (inp,x[count:])
def bre2(v):
    (v1,v2)=(bre1(v))
    (v2,v3)=bre1(v2)
    return (v1,v2,v3)
conhead=["Books","Borrowers","Checkouts"]
books=[]
borrowers=[]
checkout=[]
m=" "
while (m!="EndOfInput"):
    m=str(input())
    if (m in conhead):
        if(m==conhead[0]):
            m=str(input())
            while(m!=conhead[1]and m!=conhead[2] and m!="EndOfInput"):
                (an,t)=(bre1(m))
                books.append([an,t])
                m=str(input())
        if (m == conhead[1]):
            m=str(input())
            while (m != conhead[0] and m != conhead[2]and m!="EndOfInput"):
                (u,fn) = (bre1(m))
                borrowers.append([u, fn])
                m=str(input())
        if (m == conhead[2]):
            m=str(input())
            while (m != conhead[0] and m != conhead[1] and m!="EndOfInput"):
                (u1,an1,dd) = (bre2(m))
                checkout.append([dd,u1,an1])
                m=str(input())
AN=[]
T=[]
U=[]
FN=[]
DD=[]
checkout.sort()
for i1 in range (len(books)):
    T.append(books[i1][1])
    AN.append(books[i1][0])
for i2 in range (len(borrowers)):
    FN.append(borrowers[i2][1])
    U.append(borrowers[i2][0])
for i3 in range (len(checkout)):
    DD.append(checkout[i3][0])
DD.sort()
for j in range(len(checkout)):
    for k in range(len(FN)):
        if (checkout[j][1]==U[k]):
            checkout[j][1]=FN[k]
    for l in range(len(AN)):
        if(checkout[j][2]==AN[l]):
            checkout[j].extend([T[l]])
checkout.sort()
for z in range(len(checkout)):
    print(checkout[z][0]+"~"+checkout[z][1]+"~"+checkout[z][2]+"~"+checkout[z][3])