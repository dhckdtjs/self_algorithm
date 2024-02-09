# 평균
# score 중에서 가장 최대값 선정
# 모든 점수는 점수*100/최대값
# 더해서 평균 구하기
n = int(input())
score = list(map(int,input().split()))
Max_score = score[0]
for i in score:
    if Max_score<i:
        Max_score= i
Sum = 0
for k in score:
    Sum += (k*100)/Max_score
print(Sum/n)
