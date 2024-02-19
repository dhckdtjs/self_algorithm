# 사분면 고르기
def find_four(x,y):
    if x>0 and y>0:
        print('1')
    elif x<0 and y>0:
        print('2')
    elif x<0 and y<0:
        print('3')
    else:
        print('4')
x = int(input())
y = int(input())
find_four(x,y)