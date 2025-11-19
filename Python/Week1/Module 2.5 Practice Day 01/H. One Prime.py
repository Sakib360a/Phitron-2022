import math
def is_prime(n):
    if n<2:
        return 0
    if n==2:
        return 1
    if n%2==0:
        return 0
    for i in range(3,int(math.sqrt(n))+1,2): 
        if n%i==0:
            return 0
    return 1
n= int(input())
if is_prime(n):
    print("YES")
else:
    print("NO")