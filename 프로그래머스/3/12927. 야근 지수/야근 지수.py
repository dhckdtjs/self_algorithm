def solution(n, works):
    l = len(works)
    Max = max(works)
    work_dit = {i : 0 for i in range(Max+1)}
    for k in works:
        work_dit[k]+=1
    for t in range(n):
        work_dit[Max-1] +=1
        work_dit[Max]-=1
        if work_dit[Max] == 0:
            Max-=1
            if Max<=0:
                return 0
    total = 0
    for work in work_dit:
        if work_dit[work]:
            total+=work**2*work_dit[work]
    return total