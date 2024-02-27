# N과 M(4)

def permu(start,x):
    if x == M:
        print(*path)
        return
    for i in range(start,N+1):
        path.append(i)
        permu(i,x+1)
        path.pop()


N,M = map(int,input().split())
path = []
permu(1,0)