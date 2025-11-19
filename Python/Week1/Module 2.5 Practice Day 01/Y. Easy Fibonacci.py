n=int(input())
preFirst=0
preSecond=1
for i in range(1,n+1):
    if i==1:
        print(preFirst,end=" ")
    elif i==2:
        print(preSecond,end=" ")
    else:
        current= preFirst+preSecond
        print(current,end=" ")
        preFirst=preSecond
        preSecond=current
