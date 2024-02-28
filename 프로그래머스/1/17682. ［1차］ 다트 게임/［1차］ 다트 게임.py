
def solution(dartResult):
    res = []
    for k in range(len(dartResult)):
        answer = 0
        if dartResult[k] == 'S':
            if dartResult[k-2] == '1':
                answer = 10
            else:
                answer=int(dartResult[k-1])
            res.append(answer)
        elif dartResult[k] == 'D':
            if dartResult[k-2] == '1':
                answer = 10**2
            
            else:
                answer+=int(dartResult[k-1])**2
            res.append(answer)
        elif dartResult[k] == 'T':
            if dartResult[k-2] == '1':
                answer = 10**3
            else:
                answer+=int(dartResult[k-1])**3
            res.append(answer)
        elif dartResult[k] == '*':
            if len(res) == 1:
                one1 = res.pop()
                one1*=2
                res.append(one1)
            else:
                one2= res.pop()
                two2 = res.pop()
                one2*=2
                two2*=2
                res.append(two2)
                res.append(one2)
        elif dartResult[k] == '#':
                one3 = res.pop()
                one3 *=-1
                res.append(one3)
    answer = sum(res)
    
    return answer