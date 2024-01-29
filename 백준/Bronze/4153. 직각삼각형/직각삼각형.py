# 직각삼각형
while True:
    a,b,c = list(map(int,input().split()))
    line_list = []
    line_list.append(a)
    line_list.append(b)
    line_list.append(c)
    line_list.sort()
    max_line = line_list[-1]
    first_line = line_list[0]
    second_line = line_list[1]
    if (a,b,c) == (0,0,0):
        break
    elif max_line**2 == (first_line**2)+(second_line**2):
        print('right')
    else:
        print('wrong')
    