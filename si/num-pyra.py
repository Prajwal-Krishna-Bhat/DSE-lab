row=int(input("Enter the no:"))
a=1
for i in range(row):
    if a>row:
            break
    for k in range(i+1):
        if a>row:
            break
        print(a,"\t",end=' ')
        a+=1
    print("")