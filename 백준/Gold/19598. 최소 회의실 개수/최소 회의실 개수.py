# 최소 회의실 개수
from heapq import heappush,heappop
n = int(input())
metting = []
for i in range(n):
    st,end = map(int,input().split())
    heappush(metting,[st,end])
sort_metting = sorted(metting,key=lambda x:x[0])
metting_cnt = []
heappush(metting_cnt,sort_metting[0][1])
for m_s,m_e in sort_metting[1:]:
    if metting_cnt[0]<=m_s:
        heappop(metting_cnt)
        heappush(metting_cnt,m_e)
    else:
        heappush(metting_cnt,m_e)
print(len(metting_cnt))