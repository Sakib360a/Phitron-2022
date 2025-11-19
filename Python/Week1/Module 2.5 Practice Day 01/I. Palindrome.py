def is_pal(n):
    return str(n)==str(n)[::-1]
n=int(input())
reversed_n= int(str(n)[::-1])
if is_pal(n):
    print(reversed_n)
    print('YES')
else:
    print(reversed_n)
    print('NO')


