def sum(*args):
    sum=0
    for i in args:
        sum += i
    return sum
print(sum(20,10,30,80,100))