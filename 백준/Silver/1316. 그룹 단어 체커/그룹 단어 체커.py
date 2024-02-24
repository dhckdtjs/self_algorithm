# 그룹 단어 체커
n = int(input())
cnt = 0
for _ in range(n):
    alpha = [0]*26
    word = input()
    check_list =[]
    total =1
    for k in word:
        num = ord(k)-ord('a')
        alpha[num]+=1
    for j in range(len(alpha)):
        if alpha[j] >= 2:
            check = chr(j+ord('a'))
            check_list.append(check)
    if len(check_list)==0:
        cnt+=1
        total = 0
    else:
        for i in check_list:
            index_list = []
            for l in range(len(word)):
                if word[l] == i:
                    index_list.append(l)
            for idx in range(len(index_list)-1):
                if index_list[idx+1]-index_list[idx] != 1:
                    result = 0
                    break
                else:
                    result = 1
            total*=result
    cnt+=total
print(cnt)