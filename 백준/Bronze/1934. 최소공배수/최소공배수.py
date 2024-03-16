import sys
input = sys.stdin.readline
n = int(input().strip())

def find(num1,num2):
    res = []
    if num1 == 1 or num2 == 1:
        return [1]
    i=2
    temp = min(num1,num2)
    while i <=temp:
        if num1 % i == 0 and num2 % i == 0:
            num1 = num1//i
            num2 = num2//i
            res.append(i)
            i=2
            if num1 == 1 or num2 == 1:
                return res
        else:
            i+=1
    return res
for _ in range(n):
    A,B = map(int,input().strip().split())
    ans =1
    temp=1
    res1 = find(A,B)
    if not res1:
        ans = A*B
    else:
        for k in res1:
            temp*=k
        div1 = A//temp
        div2 = B//temp
        ans = div1*div2*temp
    print(ans)

