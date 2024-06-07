def move_fireballs(fireballs, N):
    directions = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]
    new_positions = {}

    for (r, c, m, s, d) in fireballs:
        nr = (r + s * directions[d][0] - 1) % N + 1
        nc = (c + s * directions[d][1] - 1) % N + 1
        if (nr, nc) not in new_positions:
            new_positions[(nr, nc)] = []
        new_positions[(nr, nc)].append((m, s, d))

    return new_positions


def plus_fireballs(new_positions):
    new_fireballs = []

    for (r, c), fireballs in new_positions.items():
        if len(fireballs) == 1:
            new_fireballs.append((r, c) + fireballs[0])
        else:
            total_m = sum(fb[0] for fb in fireballs)
            total_s = sum(fb[1] for fb in fireballs)
            num_fb = len(fireballs)

            if total_m // 5 > 0:
                new_m = total_m // 5
                new_s = total_s // num_fb
                even = True
                first = fireballs[0][2]%2
                for fb in fireballs:
                    if fb[2]%2 != first:
                        even = False
                        break
                if even:
                    directions = [0,2,4,6]
                else:
                    directions = [1,3,5,7]

                for d in directions:
                    new_fireballs.append((r, c, new_m, new_s, d))

    return new_fireballs


def get_fireballs(N, K, fireballs):
    for _ in range(K):
        new_positions = move_fireballs(fireballs, N)
        fireballs = plus_fireballs(new_positions)

    return sum(fb[2] for fb in fireballs)


N, M, K = map(int, input().split())
fireballs = []
for _ in range(M):
    r, c, m, s, d = map(int, input().split())
    fireballs.append((r, c, m, s, d))

result = get_fireballs(N, K, fireballs)
print(result)
