row=int(input("Enter the no of rows:"))
for i in range(row+1):
    ch=65
    for j in range(row-i):
        print(" ",end=' ')
    for k in range(i):
        print(chr(ch)," ",end=' ')
        ch+=1
    print("\n")