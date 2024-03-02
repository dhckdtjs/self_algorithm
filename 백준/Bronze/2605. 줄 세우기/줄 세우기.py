n = int(input())
num_list = list(enumerate(map(int,input().split())))
line_list = []
for i in range(n):
    line_list.insert(i-num_list[i][1],num_list[i][0]+1)
print(*line_list)