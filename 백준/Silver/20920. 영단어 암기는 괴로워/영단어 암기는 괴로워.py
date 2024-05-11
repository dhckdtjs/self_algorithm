# 영단어 암기는 괴로워
import sys
input = sys.stdin.readline
n,m = map(int,input().strip().split())
english = dict()
max_v = 0
for i in range(n):
    word = input().strip()
    if len(word)<m:
        continue
    elif len(word)>=m:
        if word not in english:
            english[word] = 1
        else:
            english[word]+=1
    if max_v<english[word]:
        max_v = english[word]
word_lst= []
while max_v >0:
    temp = []
    for k in english:
        if english[k] == max_v:
            temp.append(k)
    if len(temp)>1:
        temp.sort()
        sort_temp = sorted(temp,key=lambda x:len(x),reverse=True)
        word_lst+=sort_temp
    else:
        word_lst+=temp
    max_v-=1
for l in word_lst:
    print(l)
