H,M = list(map(int,input().split()))


if H == 0:
    if M>=45:
        print(0, M-45)
    else:
        print(23,M+15)
elif M >=45:
    print(H, M - 45)
elif M < 45:
    print(H - 1, 15 + M)

