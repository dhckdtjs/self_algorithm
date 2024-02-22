# 상수
num1,num2 = map(str,input().split())
sang_num1 = num1[::-1]
sang_num2 = num2[::-1]
if int(sang_num1)<int(sang_num2):
    print(sang_num2)
else:
    print(sang_num1)