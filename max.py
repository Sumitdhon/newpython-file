I=[]
n=int(input("enter the upper limit"))
for i in range(0,n):
    a=int(input("enter the number"))
    I.append(a)
maxno=I[0]
for i in range(0,len(I)):
    if I[i]>maxno:
        maxno=I[i]
print("the maximum number is ",maxno)