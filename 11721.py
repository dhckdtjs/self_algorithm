# 열 개씩 끊어 출력하기
str1 = input()
for i in range(0,len(str1),10):
    print(str1[i:i+10])