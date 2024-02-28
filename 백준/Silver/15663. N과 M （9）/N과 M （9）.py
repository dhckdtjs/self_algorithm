N, M = map(int, input().split())
num_list = list(map(int, input().split()))
num_list.sort()
visited = [False] * N
path = []

def permu(x):
    if x == M:
        print(*path)
        return
    
    overlap = 0
    for i in range(N):
        if not visited[i] and num_list[i] != overlap:
            visited[i] = True
            path.append(num_list[i])
            permu(x + 1)
            visited[i] = False
            path.pop()
            overlap = num_list[i]
    
permu(0)
