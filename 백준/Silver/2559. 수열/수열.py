N,K = map(int,input().split())
temp = list(map(int,input().split()))
temp1 = sum(temp[0:K])
Max_res = temp1
for i in range(N-K):
    temp1 = temp1-temp[i]+temp[i+K]
    if Max_res<temp1:
        Max_res=temp1
print(Max_res)