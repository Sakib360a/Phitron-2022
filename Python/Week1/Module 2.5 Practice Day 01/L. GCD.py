a,b= map(int,input().split())
smaller=min(a,b)
gcd=1

for i in range(smaller,0,-1):
    if(a%i==0 and b%i==0):
        gcd=i
        break
print(gcd)