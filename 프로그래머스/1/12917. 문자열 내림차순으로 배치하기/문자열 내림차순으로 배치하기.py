def solution(s):
    res = []
    for k in s:
        res.append(ord(k))
        res.sort(reverse=True)
    result = ''
    for j in res:
        result+=chr(j)
    return f"{result}"