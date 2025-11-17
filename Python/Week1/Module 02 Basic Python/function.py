#function defining:

""" def double_it(num):
    result = num*2
    return result

def sum(num1,num2):
    return num1+num2
num1=int(input("Enter the 1st number: "))
num2=int(input("Enter the 2nd number: "))
print(f"The sum is : {sum(num1,num2)}")
print(f"After doubling the sum: {double_it(sum(num1,num2))}") """

#returning multiple value as tuple from a function:
def test_function(name,section,subject,roll):
    return name,subject,section,roll
value= test_function('Sakib','B','CSE',99)
print(value)


#retruning multiple value as array:
def test_function1(name,section,subject,roll):
    return [name,subject,section,roll]
value= test_function1('Sakib','B','CSE',99)
print(value)

