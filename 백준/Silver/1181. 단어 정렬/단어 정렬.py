# 단어 정렬
N = int(input())
word_list =[]
word_list = set(word_list)
for _ in range(N):
    word = input()
    word_list.add(word)
word_list1=list(word_list)
word_list1.sort()
new_word_list = []
for i in range(1,51):
    for k in word_list1:
        cnt=0
        for j in range(len(k)):
            cnt+=1
        if cnt == i:
            new_word_list.append(k)


for k in new_word_list:
    print(k)