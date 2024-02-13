# 줄 세우기 
n = int(input())
num_list = list(map(int,input().split())) # 0 1 1 3 2  
# line_list = [i for i in range(n)]       # 1 2 3 4 5
line_list = []
line_list.append(1)
for i in range(2,n+1):
    line_list.insert((i-1)-num_list[i-1],i)
print(*line_list)