# 퇴사
# 완탐으로 하려 했으나 3번째 테케에서 오류 발생
# n = int(input())
# retire = []
# for _ in range(n):
#     day, money = map(int,input().split())
#     retire.append([day,money])

# Max_money = 0
# for i in range(n):
#     money_list = []
#     res = 0
#     while i<n:
#         if i+retire[i][0]>n:
#             break
#         money_list.append(retire[i])
#         i+=retire[i][0]
#     print(money_list)
#     for k in money_list:
#         res+=k[1]
#     if Max_money<res:
#         Max_money = res

# print(Max_money)

def dfs(n,sm):
    global ans
    if n>=N:
        ans = max(ans,sm)
        return
    
    if n+T[n]<=N:
        dfs(n+T[n],sm+P[n])
    dfs(n+1,sm)


N = int(input())
T = [0]*N
P = [0]*N
for i in range(N):
    T[i],P[i] = map(int,input().split())

ans = 0
dfs(0,0)
print(ans)