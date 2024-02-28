# N과 M(6)
N,M = map(int,input().split())
num_list = list(map(int,input().split()))
num_list.sort()
path = []
def permu(start,x):
    if x == M:
        print(*path)
        return
    for i in range(start,N):
        path.append(num_list[i])
        permu(i+1,x+1)
        path.pop()
permu(0,0)