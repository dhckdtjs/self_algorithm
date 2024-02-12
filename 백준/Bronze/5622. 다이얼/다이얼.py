# 다이얼
# 숫자 1을 걸려면 총 2초
dic = {'1':2,'A,B,C' : 3,'D,E,F':4,'G,H,I':5,'J,K,L':6,'M,N,O':7,'P,Q,R,S':8,'T,U,V':9,'W,X,Y,Z':10}
word = input()
dial = 0
for k in word:
    for j in dic.keys():
        if k in j:
            dial+=dic[j]
print(dial)
