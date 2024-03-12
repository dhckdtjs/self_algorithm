num = [0]*5
for i in range(5):
    n = int(input())
    num[i] = n
num.sort()
print(sum(num)//5)
print(num[2])