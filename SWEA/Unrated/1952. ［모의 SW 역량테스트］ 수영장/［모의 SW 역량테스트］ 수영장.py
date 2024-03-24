T = int(input())


for tc in range(1,T+1):
    day,mon,mon_3,year = map(int,input().split())
    cal = [0]+list(map(int,input().split()))
    DP = [0] * 13
    for i in range(1, 13):
        mn = DP[i - 1] + day * cal[i]
        mn = min(mn, DP[i - 1] + mon)
        if i >= 3:
            mn = min(mn, DP[i - 3] + mon_3)
        if i >= 12:
            mn = min(mn, DP[i - 12] + year)
        DP[i] = mn

    print(f'#{tc} {DP[-1]}')