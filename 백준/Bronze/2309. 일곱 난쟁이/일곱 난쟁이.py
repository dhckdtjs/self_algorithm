little_list = []

def powerset(idx):
    s = 0
    global result
    res = []
    if idx == N:
        for i in range(N):
            if c[i]:
                s+=little_list[i]
                res.append(little_list[i])
                if s>100:
                    return
        if len(res) == 7 and s == 100:
            result = res
        return

    c[idx] = 0
    powerset(idx+1)
    c[idx] = 1
    powerset(idx+1)



for _ in range(9):
    little = int(input())
    little_list.append(little)
little_list.sort()
N = len(little_list)
c = [0]*N
result = []
powerset(0)
for k in result:
    print(k)