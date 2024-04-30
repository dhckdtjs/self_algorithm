# ZOAC 4
h,w,n,m = map(int,input().split())
start_w = 0
start_h = 0
cnt_w = 1
cnt_h = 1
while True:
    start_w+=m+1
    if start_w >=w:
        break
    cnt_w+=1
while True:
    start_h+=n+1
    if start_h>=h:
        break
    cnt_h+=1
print(cnt_w*cnt_h)