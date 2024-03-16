import sys
input = sys.stdin.readline

def find(num1,num2):
    global res
    i =2
    if num1 ==1 or num2 == 1:
        res = [1]
        return res
    while num1 !=1 and num2 !=1:
        if num1 %i == 0 and num2%i == 0:
            num1 = num1//i
            num2 = num2//i
            res.append(i)
            i = 2
        else:
            i+=1
        if i >num1 or i>num2:
            break


a,b = map(int,input().strip().split())
res = []
find(a,b)
ans = 1
if not res:
    print(a*b)
else:
    for k in res:
        ans*=k
    print(a*b//ans)
