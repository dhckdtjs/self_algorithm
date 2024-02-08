def numbering_num(num1,num2):
    num_list = []
    num_list.append(num1)
    while num2>=0:
        num_list.append(num2)
        num1,num2 = num2,num1-num2
    return num_list

n= int(input())
length = 0
for k in range(n,-1,-1):
    result = numbering_num(n,k)
    if length<=len(result):
        length = len(result)
        Max_result = result
    else:
        break

print(length)
print(*Max_result)