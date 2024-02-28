# N과 M(12)
def permu(start,x):
    if x == M:
        print(*path)
        return
    
    overlap = 0
    for i in range(start,N):
        if overlap != num_list[i]:
            path.append(num_list[i])
            permu(i,x+1)
            path.pop()
            overlap = num_list[i]


N,M = map(int,input().split())
num_list = list(map(int,input().split()))
num_list.sort()
path = []
permu(0,0)