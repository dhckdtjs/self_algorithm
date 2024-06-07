def solution(A, B):
    A.sort()
    B.sort()
    cnt = 0
    j=0
    for a in A:
        # Find the first card in B that can beat the card in A
        while j < len(B) and B[j] <= a:
            j += 1
        if j < len(B):
            cnt += 1
            j += 1
    return cnt