arr=[]
n=int(input("Enter the size of list:"))
for i in range(n):
    arr.append(int(input(f"Enter the value {i}:")))
key=int(input("Enter the key to search:"))
for i in range(n):
    if arr[i]==key:
        print("the value exists in list!")
        break
print("Error 404! key not in list!")