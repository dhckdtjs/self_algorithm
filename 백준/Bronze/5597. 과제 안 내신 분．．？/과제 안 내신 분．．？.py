# 과제 안 내신 분?
total = [i for i in range(1,31)]
for i in range(28):
    person = int(input())
    if person in total:
        total.remove(person)
print(total[0])
print(total[1])
