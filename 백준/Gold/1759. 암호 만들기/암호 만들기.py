# 암호 만들기
from itertools import combinations
l,c = map(int,input().split())

vowel = {'a','e','i','o','u'}

alpha = list((input().split()))
alpha.sort()

for t in combinations(alpha,l):
    cnt1,cnt2 = 0,0
    for q in t:
        if q in vowel:
            cnt1+=1
        else:
            cnt2+=1
    if cnt1 >=1 and cnt2>=2:
        print(''.join(t))
