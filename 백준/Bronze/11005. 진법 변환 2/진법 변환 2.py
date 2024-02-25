# 진법 변환 2
N,B = map(int,input().split())
sen = ''
change = {10:'A',11:'B',
          12:'C',13:'D',
          14:'E',15:'F',
          16:'G',17:'H',
          18:'I',19:'J',
          20:'K',21:'L',
          22:'M',23:'N',
          24:'O',25:'P',
          26:'Q',27:'R',
          28:'S',29:'T',
          30:'U',31:'V',
          32:'W',33:'X',
          34:'Y',35:'Z',}
while N>0:
    if N == 1:
        sen='1'+sen
        break
    div = N%B
    if div in change:
        sen =str(change[div])+sen
    else:
        sen=str(div)+sen
    N = N//B
print(sen)
