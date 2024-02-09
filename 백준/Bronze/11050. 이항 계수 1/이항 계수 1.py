# 이항 계수1
# 자연수 N과 정수 K가 주어졌을 때 이항 계수를 구하는 프로그램 작성
N,K = map(int,input().split())
mom = 1                     # 분모
son = 1                     # 분자
for i in range(N,N-K,-1):
    son *=i
for j in range(K,0,-1):
    mom*=j
print(int(son/mom))