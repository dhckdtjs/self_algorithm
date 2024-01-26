T = int(input())
for _ in range(T):
    a, sen = list(map(str,input().split()))
    for k in sen:
        print(int(a)*k,end='')
    print()