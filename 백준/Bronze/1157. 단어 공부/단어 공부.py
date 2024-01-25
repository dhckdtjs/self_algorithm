str = input()
uStr = str.upper()

alphabets = [0] * 26
ft_max = 0
cnt = 0
c = '?'


for i in uStr : 
    alpha = ord(i)
    alphabets[alpha - ord('A')] += 1
for k in alphabets :
    if(ft_max < k):
        ft_max = k

for i in range(0,len(alphabets)) : 
    if(ft_max == alphabets[i]):
        c = chr(i + ord('A'))
        cnt += 1

if cnt > 1 :
    print('?')
else : 
    print(c)