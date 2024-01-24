# 숫자의 합
N = int(input())
sum= 0
num = list(map(str,input()))
for k in num:
    sum+=int(k)
print(sum)