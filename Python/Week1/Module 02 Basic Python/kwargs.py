#args
def sum(*args):
    sum=0
    for i in args:
        sum += i
    return sum
print("This is the example of args:")
print(f"Sum is: {sum(20,10,30,80)}")

print("This is the example of kargs:")
#kargs or kwargs
def information(**kargs):
    for key,value in kargs.items():
        print(key,":",value)

information(name='Sakib',age=25, roll= 99, subject='CSE', semester='7th', section='B')