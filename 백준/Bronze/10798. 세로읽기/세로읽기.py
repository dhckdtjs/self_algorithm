# 세로 읽기
arr = [list(input()) for _ in range(5)]
Max= 0
for k in range(5):
    N = len(arr[k])
    if Max<N:
        Max =N 
for i in arr:
    if len(i) !=Max:
        for _ in range(Max-len(i)):
            i.append('')
for i in range(Max):
    for j in range(5):
        print(arr[j][i],end='')
print()