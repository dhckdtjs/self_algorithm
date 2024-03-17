# 다음 소수
import sys
import math
input =sys.stdin.readline
T = int(input())
for tc in range(1,T+1):
    num = int(input())
    if num == 1 or num == 0:
        print(2)
        continue
    while True:
        flag = 0
        for i in range(2,int(math.sqrt(num))+1):
            if num%i == 0:
                num+=1
                flag+=1
                break
        if flag == 0:
            print(num)
            break
