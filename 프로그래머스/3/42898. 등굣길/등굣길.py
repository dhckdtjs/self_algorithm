def solution(m, n, puddles):
    dp = [[0] * m for _ in range(n)]
    dp[0][0] = 1
    puddles = set(tuple(puddle) for puddle in puddles)
    print(puddles)
    for i in range(n):
        for j in range(m):
            if (j + 1, i + 1) in puddles:
                dp[i][j] = 0
            else:
                if i > 0:
                    dp[i][j] += dp[i - 1][j]
                if j > 0:
                    dp[i][j] += dp[i][j - 1]
    
    return dp[n - 1][m - 1] % 1000000007

m = 4
n = 3
puddles = [[2, 2]]
print(solution(m, n, puddles))
