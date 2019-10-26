x=[]
for i in range(int(input())):
    y=[]
    name = input()
    score = float(input())
    y.append(score)
    y.append(name)
    x.append(y)
sorted(x)
print(x)
if x[0][0]==x[1][0]:
    print(x[0][1])
    print(x[1][1])
else:
    print(x[0][1])
print("rajessh")
print("raju")
