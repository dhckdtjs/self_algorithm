# 4와 7
n = int(input())
temp = str(bin(n+1)[2:])
res = temp[1:]
total = ''
for k in res:
    if k == '0':
        total+='4'
    else:
        total+='7'
print(total)