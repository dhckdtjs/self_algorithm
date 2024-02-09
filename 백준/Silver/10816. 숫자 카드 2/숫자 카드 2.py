import sys
input = sys.stdin.readline
N = int(input())
card_list = list(map(int,input().split()))
M = int(input())
counts = [0]*M
M_list = list(map(int,input().split()))
card_list.sort()
# selection_sort(card_list,N)
dic = {}
for card in card_list:
    if card in dic:
        dic[card]+=1
    else:
        dic[card] = 1
for k in M_list:
    if k in dic:
        print(dic[k],end=' ')
    else:
        print(0,end=' ')