cal = input().split('-')
num1 = []
for i in cal:
    sum = 0
    num = i.split('+')
    for j in num:
        sum+=int(j)
    num1.append(sum)

n = num1[0]
for k in num1[1:]:
    n-=k
print(n)