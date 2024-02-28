# 약수들의 합
while True:
    
    res = []
    n = int(input())
    if n == -1:
        break
    for i in range(1,n+1):
        if n%i == 0:
            res.append(i)
    res.pop()
    s = 0
    for k in range(len(res)):
        s+=res[k]
    if s == n:
        print(f'{n} =',end=' ')
        for k in range(len(res)):
            print(res[k],end=' ')
            if k<=len(res)-2:
                print('+',end=' ')
        print()
    else:
        print(f'{n} is NOT perfect.')