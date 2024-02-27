# 설탕배달
n = int(input())
sugar = [5,3]
i = 0
j = 0
res = []
while 5*i<=n:
    for j in range((n//3)+1):
        if 5*i+3*j == n:
            res.append([i,j])
    i+=1

min_v = 5000
if len(res) == 0:
    print(-1)
else:
    for k in range(len(res)):
        result = res[k][0]+res[k][1]
        if min_v>result:
            min_v = result
    print(min_v)