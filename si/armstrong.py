num=int(input("Enter the number to check armstrong nature:"))
x=num
length=1
while x>1:
    x=x//10
    length+=1
x=num
result=0
for i in range(length):
    digit=x%10
    result+=digit**length
    x=x//10
if result==num:
    print("Entered number is an armstrong number")
else:
    print("Not an armstrong number")
