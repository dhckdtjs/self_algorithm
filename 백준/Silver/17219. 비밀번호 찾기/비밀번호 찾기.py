# 비밀번호 찾기
import sys
input = sys.stdin.readline
n,m = map(int,input().split())
site_dict ={}
for i in range(n):
    site,pw = input().split()
    site_dict[site] = pw
for j in range(m):
    quest = input().rstrip()
    if quest in site_dict:
        print(site_dict[quest])