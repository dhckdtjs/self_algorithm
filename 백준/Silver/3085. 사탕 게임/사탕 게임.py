n = int(input())
candy = [list(input())+[0] for _ in range(n)]+[[0]*(n+1)]
candy_t = list(map(list,zip(*candy)))

def count(lst):
    cnt = ans =1
    for i in range(1,len(lst)):
        if lst[i] == lst[i-1]:
            cnt+=1
            ans = max(cnt,ans)
        else:
            cnt = 1
    return ans

def solve(arr):
    mx = 0
    for i in range(n-1):
        for j in range(0,n):
            arr[i][j],arr[i][j+1] = arr[i][j+1],arr[i][j]
            mx = max(mx,count(arr[i])) 
            arr[i][j],arr[i][j+1] = arr[i][j+1],arr[i][j]

            arr[i][j],arr[i+1][j] = arr[i+1][j],arr[i][j]
            mx = max(mx,count(arr[i]),count(arr[i+1]))
            arr[i][j],arr[i+1][j] = arr[i+1][j],arr[i][j]
    return mx
ans = max(solve(candy), solve(candy_t))
print(ans)