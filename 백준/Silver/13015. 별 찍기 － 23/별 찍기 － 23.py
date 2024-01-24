import sys
input = sys.stdin.readline
n = int(input())
mid = 2*n-3
side = 1
print("*"*n+" "*mid+"*"*n)
mid-=2
for i in range(n-2):
    print(" "*side+"*"+" "*(n-2)+"*"+" "*mid+"*"+" "*(n-2)+"*")
    mid-=2
    side+=1
print(" "*(n-1)+"*"+" "*(n-2)+"*"+" "*(n-2)+"*")
for i in range(n-2):
    side-=1
    mid+=2
    print(" "*side+"*"+" "*(n-2)+"*"+" "*mid+"*"+" "*(n-2)+"*")
mid+=2
print("*"*n+" "*mid+"*"*n)