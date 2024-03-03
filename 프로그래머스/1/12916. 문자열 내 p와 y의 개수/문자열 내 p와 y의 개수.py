def solution(s):
    global cnt1
    global cnt2
    s = s.lower()
    cnt1 = 0
    cnt2 = 0
    for k in s:
        if k == 'p':
            cnt1+=1
        elif k == 'y':
            cnt2+=1
    if cnt1 == cnt2:
        return True
    else:
        return False