# 삼각형 외우기
triangle = []
for _ in range(3):
    n = int(input())
    triangle.append(n)
if triangle.count(60)==3:
    print('Equilateral')
elif sum(triangle) !=180:
    print('Error')
elif sum(triangle) == 180:
    if triangle[0] == triangle[1] or triangle[1] == triangle[2] or triangle[0] == triangle[2]:
        print('Isosceles')
    elif triangle[0] !=triangle[1] and triangle[1] != triangle[2] and triangle[2] != triangle[0]:
        print('Scalene')
