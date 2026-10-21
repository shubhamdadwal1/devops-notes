n1=int(input("enter the first value: "))
n2=int(input("enter the second value: "))
print(type(n1))
print(type(n2))
print("1. add")
print("2. subtraction")
print("3. Multipication")
print("4. divide")
choice=int(input("enter the one number:"))
if choice ==1:
    print("result",n1+n2)
elif choice==2:
    print("result",n1-n2)
elif choice==3:
    print("result",n1*n2)
elif choice==4:
    if n2 !=0:
        print("result",n1/n2)
    else:
        print("not divide into zero")
else:
    print("choice one number")

