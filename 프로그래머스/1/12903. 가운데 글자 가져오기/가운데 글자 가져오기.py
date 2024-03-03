def solution(s):
    answer = ''
    N = len(s)
    if N%2 == 0:
        answer+=s[N//2-1]+s[N//2]
    else:
        answer+=s[N//2]
    return answer