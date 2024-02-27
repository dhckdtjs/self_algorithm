# N과 M (2)
def permu(start, x):
    if x == M:
        print(*path)
        return
    for i in range(start, N+1):
        path.append(i)
        permu(i+1, x+1)  # 다음 숫자는 현재 선택한 숫자보다 커야 하므로 i+1부터 시작
        path.pop()

N, M = map(int, input().split())
path = []
permu(1, 0)