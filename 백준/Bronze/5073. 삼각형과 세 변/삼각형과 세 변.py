# 삼각형과 세 변
while True:
    triangle = list(map(int,input().split()))
    if sum(triangle) == 0:
        break
    else:
        a = triangle[0]
        b = triangle[1]
        c = triangle[2]
        sum2 = sum(triangle)-max(triangle)
        
        if a==b==c:
            print('Equilateral')
        elif max(a,b,c)>=sum2:
            print('Invalid')
        elif a!=b and b!=c and c!=a:
            print('Scalene')
        
        elif a==b or b==c or c==a:
            print('Isosceles')
