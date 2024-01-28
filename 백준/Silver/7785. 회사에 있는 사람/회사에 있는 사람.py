# 회사에 있는 사람
import sys
input = sys.stdin.readline
log = int(input())
enter_list = set()
for k in range(log):
    enter = list(map(str,input().split()))
    if enter[1] =='enter':
        enter_list.add(enter[0])
    else:
        enter_list.remove(enter[0])
final = sorted(enter_list,reverse=True)
for j in final:
    print(j)
