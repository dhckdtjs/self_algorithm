# 영화감독 숌
# 666숫자가 들어가도록 배열 만들기
# 번째 수가 주어지면 그에 맞는 숫자 출력
n = int(input())
cnt = 0
result = 666
while True:
    if '666'in str(result):
        cnt+=1
    
    if cnt == n:
        print(result)
        break
    result+=1
