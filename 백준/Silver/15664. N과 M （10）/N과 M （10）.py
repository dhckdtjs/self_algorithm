# N과 M(10)

def permu(start,x):
    if x== M:
        print(*path)
        return
    
    overlap = 0
    for i in range(start,N):
        if visited[i] == True or num_list[i] == overlap:
            continue
        visited[i]= True
        path.append(num_list[i])
        permu(i+1,x+1)
        visited[i] = False
        path.pop()
        overlap =num_list[i]
            

N,M = map(int,input().split())
num_list= list(map(int,input().split()))
num_list.sort()
visited = [False]*N
path = []
permu(0,0)