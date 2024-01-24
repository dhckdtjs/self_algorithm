T = int(input())
for i in range(1,2*T):
    if i<=T:
        print("*"*i+" "*2*(T-i)+"*"*i)
    else:
        print("*"*(2*T-i)+" "*2*(i-T)+"*"*(2*T-i))