# 모음의 개수
collection = ['a','e','i','o','u','A','E','I','O','U']
while True:
    word = input()
    cnt=0
    
    if word == '#':
        break
    for i in word:
        if i in collection:
            cnt+=1
    print(cnt)