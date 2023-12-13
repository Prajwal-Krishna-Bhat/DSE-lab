row=int(input("Enter the no of rows:"))
for i in range(row):
    ch=65
    print("  " * (row-i), end=" ")
    for k in range(i+1):
        print(chr(ch)," ",end=' ')
        ch+=1
    print("\n")