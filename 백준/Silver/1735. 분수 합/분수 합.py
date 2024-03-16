# 분수 합
import sys
input = sys.stdin.readline

def check(num1,num2):
    while num2 !=0:
        num1,num2 = num2,num1%num2
    return num1

son_a,mom_a = map(int,input().strip().split())
son_b,mom_b = map(int,input().strip().split())
temp_m = mom_a*mom_b
temp_s = (temp_m//mom_a)*son_a+(temp_m//mom_b)*son_b
res = check(temp_s,temp_m)
ans_m = temp_m//res
ans_s = temp_s//res
print(ans_s,ans_m)