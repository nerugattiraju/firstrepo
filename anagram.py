#write a program to find the anagaram words between two text files
f1=open('e:/1.txt','rb')
f1=f1.read()
f1=str(f1)
f2=open('e:/2.txt','rb')
f2=f2.read()
f2=str(f2)
a=f1.split(" ")
b=f2.split(" ")
for i in a:
    for j in b:
        if(sorted(i)==sorted(j)):
            print(j)
            
