# 나이순 정렬
# 나이와 이름이 가입한 순서대로 주어짐
# 나이가 증가하는 순으로 나이가 같으면 먼저 가입한 사람이 앞에 오는 순서로 정렬
import sys
input = sys.stdin.readline
n = int(input())
online_list = []
for _ in range(n):
    age,name =input().split()
    age = int(age)
    online_list.append([age,name])
online_list = sorted(online_list,key= lambda x:x[0])
for k in online_list:
    print(*k)