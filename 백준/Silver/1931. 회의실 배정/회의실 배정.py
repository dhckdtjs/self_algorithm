n = int(input())
meeting_list = []
for _ in range(n):
    S,E = map(int,input().split())
    meeting_list.append([S,E])
tmp = sorted(meeting_list,key = lambda x:x[0])
sort_meeting = sorted(tmp,key = lambda x:x[1])
start_meeting = sort_meeting[0][0]
end_meeting = sort_meeting[0][1]
cnt = 1
for start,end in sort_meeting[1:]:
    if start>=end_meeting:
        cnt+=1
        end_meeting = end
print(cnt)