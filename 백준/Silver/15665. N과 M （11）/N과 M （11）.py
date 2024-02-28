# N과 M (11)
N,M = map(int,input().split())
num_list = list(map(int,input().split()))
num_list.sort()
path = []
def permu(x):
    if x== M:
        print(*path)
        return
    
    before = 0
    for i in range(N):
        if before == num_list[i]:
            continue
        path.append(num_list[i])
        permu(x+1)
        path.pop()
        before = num_list[i]


permu(0)