# 부녀회장이 될테야
T = int(input())

    
def check_person(x,y):
    person = [i for i in range(1,ho+1)]
    for i in range(floor):
        for j in range(1,ho):
                person[j] +=person[j-1]
    return person[-1]
for tc in range(1,T+1):
    floor = int(input())
    ho = int(input())
    result = check_person(floor,ho)
    print(result)