n = int(input())
meeting_list = []
for _ in range(n):
    S,E = map(int,input().split())
    meeting_list.append((S,E))
tmp = sorted(meeting_list,key=lambda x:x[0])
sort_meeting = sorted(tmp,key=lambda x:x[1])
first_s = sort_meeting[0][0]
first_e = sort_meeting[0][1]
cnt = 1
for start,end in sort_meeting[1:]:
    if first_e<=start:
        cnt+=1
        first_s = start
        first_e = end
print(cnt)