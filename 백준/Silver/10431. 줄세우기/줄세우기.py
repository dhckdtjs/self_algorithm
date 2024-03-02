T = int(input())
n = 20
for tc in range(1,T+1):
    test_case, *child = list(map(int,input().split()))
    cnt = 0
    for i in range(n-1,-1,-1):
        for j in range(i):
            if child[j]>child[j+1]:
                child[j],child[j+1] = child[j+1],child[j]
                cnt+=1
    print(f'{test_case} {cnt}')