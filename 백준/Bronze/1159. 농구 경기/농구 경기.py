# 농구 경기
n = int(input())
name_list=[]
alphabets = [0]*26
first_list = []
for name in range(n):
    name = input()
    name_list.append(name)
for k in name_list:
    first = k[0]
    data = ord(first) - ord('a')
    first_list.append(data)
for i in first_list:
    alphabets[i]+=1
for h in range(len(alphabets)):
    if alphabets[h] >=5:
        print(chr(h+97),end='')
if max(alphabets)<5:
        print('PREDAJA')   

# A 65
# a 91 or 