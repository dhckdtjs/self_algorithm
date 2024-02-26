# 소수
M = int(input())
N = int(input())
def find_prime(num):
    if num == 1:
        return 0
    for i in range(2,num):
        if num% i == 0:
            return 0
    return 1
prime_list = []
for k in range(M,N+1):
    res = find_prime(k)
    if res == 1:
        prime_list.append(k)
if len(prime_list) == 0:
    print(-1)
else:
    print(sum(prime_list))
    print(min(prime_list))