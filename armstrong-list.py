a=int(input("Enter the range:"))
list=[]
for i in range(a):
    num=i
    x=num
    length=0
    while x>=1:
        x=x//10
        length+=1
    x=num
    result=0
    for i in range(length):
        result+=(x%10)**length
        x=x//10
    if result==num:
        list.append(num)
print("The armstrong numbers are:",list)