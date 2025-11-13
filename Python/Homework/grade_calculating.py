num= float(input("Enter the number: "))

if 80<= num<=100:
    print("A+")
elif 70<=num<80:
    print("A")
elif 60<=num<70:
    print("A-")
elif 50<=num<60:
    print("B")
elif 40<=num<50:
    print("C")
elif 33<=num<40:
    print("D")
elif 0<=num<33:
    print("F")
else:
    print("Invalid Number")