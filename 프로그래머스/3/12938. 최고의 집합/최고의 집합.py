def solution(n, s):
    if s < n:
        return [-1]
    
    div, r = divmod(s, n)
    print(div,r)
    result = [div] * n
    
    for i in range(r):
        result[i] += 1
    
    return sorted(result)
