import sys
from heapq import heappop, heappush

input = sys.stdin.readline
n, d = map(int, input().strip().split())


def dijkstra(graph, d):
    distance = [float('inf')] * (d + 1)
    pq = []
    heappush(pq, (0, 0))
    distance[0] = 0

    while pq:
        dist, now = heappop(pq)
        if distance[now] < dist:
            continue

        if now < d and distance[now + 1] > dist + 1:
            distance[now + 1] = dist + 1
            heappush(pq, (dist + 1, now + 1))

        for next_node, next_cost in graph[now]:
            if next_node <= d:
                new_cost = dist + next_cost
                if new_cost < distance[next_node]:
                    distance[next_node] = new_cost
                    heappush(pq, (new_cost, next_node))

    return distance[d]


graph = [[] for _ in range(d + 1)]
for _ in range(n):
    st, ed, l = map(int, input().strip().split())
    if ed <= d:
        graph[st].append((ed, l))

min_distance = dijkstra(graph, d)
print(min_distance)
