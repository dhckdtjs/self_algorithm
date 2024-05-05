def solution(n, works):
    l = len(works)
    maxx = max(works)
    work_dict = {i:0 for i in range(maxx+1) }
    for w in works:
        work_dict[w]+=1
    res = 0
    for t in range(n):
        if maxx>0:
            work_dict[maxx] -=1
            work_dict[maxx-1] +=1
            if not work_dict[maxx]:
                maxx-=1
        else:
            break
    for num in work_dict:
        res += num**2*work_dict[num]
                
    return res