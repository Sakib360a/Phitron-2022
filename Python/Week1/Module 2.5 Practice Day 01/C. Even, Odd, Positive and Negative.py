n=int(input())
nums = list(map(int,input().split()))
even=odd=positive=negative=0
for num in nums:
    if num%2==0:
        even+=1
    else:
        odd+=1
    if num>0:
        positive+=1
    elif num<0:
        negative+=1
print(f"Even: {even}")
print(f"Odd: {odd}")
print(f"Positive: {positive}")
print(f"Negative: {negative}")