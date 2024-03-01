W,H = map(int,input().split())
n = int(input())
w_list = [0,W]
h_list = [0,H]
for _ in range(n):
    direct, num = map(int,input().split())
    if direct == 0:
        h_list.append(num)
    else:
        w_list.append(num)
w_list.sort(reverse=True),h_list.sort(reverse=True)
Max_w = 0
Max_h = 0
for i in range(len(w_list)-1):
    width = w_list[i]-w_list[i+1]
    if Max_w<width:
        Max_w = width
for j in range(len(h_list)-1):
    height = h_list[j]-h_list[j+1]
    if Max_h<height:
        Max_h= height
print(Max_w*Max_h)