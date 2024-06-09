def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, rank, x, y):
    rootx = find(parent, x)
    rooty = find(parent, y)

    if rootx != rooty:
        if rank[rootx] > rank[rooty]:
            parent[rooty] = rootx
        elif rank[rootx] < rank[rooty]:
            parent[rootx] = rooty
        else:
            parent[rooty] = rootx
            rank[rootx] += 1

n, m = map(int, input().split())
parent = list(range(n + 1))
rank = [0] * (n + 1)

results = []

for _ in range(m):
    num, a, b = map(int, input().split())
    if num == 0:
        union(parent, rank, a, b)
    elif num == 1:
        if find(parent, a) == find(parent, b):
            results.append("YES")
        else:
            results.append("NO")

for result in results:
    print(result)
