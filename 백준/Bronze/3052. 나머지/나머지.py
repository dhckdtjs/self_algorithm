lst= []
same=[]
cnt= 0
for _ in range(10):
    num = int(input())
    result = num % 42
    lst.append(result)
for i in lst:
    if i not in same:
        cnt+=1
        same.append(i)
print(cnt)