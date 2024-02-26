def solution(n):
    cnt = 0
    for num in range(2,n+1):
        for j in range(2,int((num)**0.5)+1):
            if num%j == 0:
                break
        else:
            cnt+=1
    return cnt