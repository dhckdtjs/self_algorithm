# 서로 다른 부분 문자열의 개수
import sys
input = sys.stdin.readline

word = input().strip()
N = len(word)
i =1
S = set()
while i <=N:
    for j in range(N+1-i):
        W = ''
        W+=word[j:j+i]
        S.add(W)
    i+=1
print(len(S))