number = [10,20,30,40,50,60,70,80,90,100]
""" n = int(input("How many value you want to insert:"))
for i in range(n):
    value= int(input(f"Enter {i}-th value:"))
    number.append(value)

for i in range(n):
    print(f"The value of {i} is:",number[i])
 """

print(number[1:10])
print(number[1:10:2])
print(number[10:0:-2])
print(number[:3])# didnt mention start, it will start from the beginning automatically
print(number[1::2]) # mentioned start and didnt mention end but it will print till end automatically
print(number[:]) # printing list without defining the range to print, it will start from begining to end
print(number[::-1]) # shortcut to reverse a list