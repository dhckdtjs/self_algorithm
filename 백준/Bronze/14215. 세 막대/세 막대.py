# 세 막대
import sys
input = sys.stdin.readline
triangle = list(map(int,input().split()))
mx = max(triangle)
sum2 = sum(triangle)-mx
if mx>=sum2:
    print(sum2+sum2-1)
elif triangle[0]==triangle[1]==triangle[2]:
    print(triangle[0]*3)    
elif sum2>mx:
    print(sum(triangle))