def solution(numbers):
    numbers.sort()
    n = len(numbers)
    answer = []
    for i in range(n-1,0,-1):
        for j in range(i):
            res = numbers[i]+numbers[j]
            if res in answer:
                continue
            else:
                answer.append(res)
    answer.sort()
    return answer