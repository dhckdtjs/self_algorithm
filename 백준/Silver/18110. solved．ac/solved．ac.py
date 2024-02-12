# solved.ac
# 난이도 의견이 주어지면 위 15%, 아래 15% 제외하고 평균 구하기
# 평균 반올림, 제외된 사람 수 역시 반올림
def up_or_down(n):
    if n-int(n)>=0.5:
        result = int(n)+1
    else:
        result = int(n)
    return result

import sys
input = sys.stdin.readline
n = int(input())
grade_list = []
temp= n*0.15

for _ in range(n):
    grade = int(input())
    grade_list.append(grade)
re_idx = up_or_down(temp)
grade_list.sort()
Sum = 0
for i in range(re_idx,n-re_idx):
    Sum+=grade_list[i]
if len(grade_list) == 0:
    res = 0
elif n == 0:
    res = 0
else:
    res = Sum/((len(grade_list)-re_idx*2))

print(up_or_down(res))