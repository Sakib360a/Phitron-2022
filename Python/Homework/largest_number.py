num1= float(input("Enter the 1st number: "))
num2= float(input("Enter the 2nd number: "))
num3= float(input("Enter the 3rd number: "))

if num1>num2:
    if num1>num3:
        print(f"{num1} is the largest number")
    else:
        print(f"{num3} is the largest number")
elif num2>num1:
    if num2>num3:
        print(f"{num2} is the largest number")
    else:
        print(f"{num3} is the largest number")
else:
    print(f"{num3} is the largest number")
    