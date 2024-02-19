# 같은 눈 3개 나오면 10,000원 +(같은 눈)*1000
# 2개 나오면 1000+같은눈*100원
# 다른 눈 가장 큰 눈*100
counts=[0]*7
A,B,C = map(int,input().split())
Max = 0
for k in A,B,C:
    counts[k]+=1
for i in range(7):
    if counts[i] == 3:
        money = 10000+i*1000
        break
    elif counts[i] == 2:
        money = 1000+i*100
        break
    elif counts[i] == 1:
        if Max<i:
            Max = i
        money = Max*100
print(money)