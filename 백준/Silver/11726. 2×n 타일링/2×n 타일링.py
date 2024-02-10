# 2xn 타일링
# DP를 사용해서 풀자
# 점화식을 생각
def paper_sum(n):
    paper = [0]*(n+1)
    paper[0] = 1
    paper[1] = 1
    for i in range(2,n+1):
        paper[i] = paper[i-1]+paper[i-2]
    return paper[-1]


n = int(input())
result = paper_sum(n)
print(result%10007)