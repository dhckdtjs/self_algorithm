# Hashing
n = int(input())
string = str(input())
hashing_dic={'a':1,'b':2,'c':3,'d':4,'e':5,
             'f':6,'g':7,'h':8,'i':9,'j':10,
             'k':11,'l':12,'m':13,'n':14,'o':15,
             'p':16,'q':17,'r':18,'s':19,'t':20,
             'u':21,'v':22,'w':23,'x':24,'y':25,
             'z':26}
res = 0
for k in range(len(string)):
    if string[k] in hashing_dic:
        res+=31**(k)*hashing_dic.get(string[k])
print(res%1234567891)