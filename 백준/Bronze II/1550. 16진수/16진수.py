# 16진수
num = input()
res = 0
length = len(num)
for k in num:
    if length == 0:
        break
    if k == 'A':
        res+=16**(length-1)*10
    elif k == 'B':
        res+=16**(length-1)*11
    elif k == 'C':
        res+=16**(length-1)*12
    elif k == 'D':
        res+=16**(length-1)*13
    elif k == 'E':
        res+=16**(length-1)*14
    elif k == 'F':
        res+=16**(length-1)*15
    else:
        res+=16**(length-1)*int(k)
    length-=1
print(res)