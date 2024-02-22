# 크로아티아 알파벳
sen = input()
crot_list = ['c=','c-','dz=','d-','lj','nj','s=','z=']
i = 0
cnt = 0
while i <len(sen):
    check = sen[i:i+2]
    check3 = sen[i:i+3]
    if check3 in crot_list:
        cnt+=1
        i+=3
    elif check in crot_list:
        cnt+=1
        i+=2
    else:
        cnt+=1
        i+=1
print(cnt)