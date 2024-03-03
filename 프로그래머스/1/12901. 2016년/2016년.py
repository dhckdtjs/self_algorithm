def solution(a, b):
    if a == 1:
        day = b
    elif a == 2:
        day = 31+b
    elif a == 3 or a==4:
        day = 31*(a-2)+29+b
    elif a == 5 or a==6:
        day = 31*(a-3)+29+30+b
    elif a == 7 or a==8 or a== 9:
        day = 31*(a-4)+29+30*2+b
    elif a == 10 or a== 11:
        day = 31*(a-5)+29+30*3+b
    elif a == 12:
        day = 31*6+30*4+29+b
    if day % 7 == 1:
        answer = 'FRI'
    elif day %7 == 2:
        answer = 'SAT'
    elif day % 7 == 3:
        answer = 'SUN'
    elif day % 7 == 4:
        answer = 'MON'
    elif day % 7== 5:
        answer = 'TUE'
    elif day % 7 == 6:
        answer = 'WED'
    else:
        answer = 'THU'         
    return answer