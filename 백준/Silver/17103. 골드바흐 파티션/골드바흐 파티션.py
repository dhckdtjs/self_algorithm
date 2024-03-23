import sys
input = sys.stdin.readline
n = int(input())

lst = [0,0]+[1]*(999999)
for i in range(2,len(lst)):
    if lst[i]:
        for j in range(i*2,len(lst),i):
            lst[j] = 0

for i in range(n):
    num = int(input())

    cnt = 0
    for j in range(2,num//2+1):
        if lst[j] and lst[num-j]:
            cnt+=1
    print(cnt)