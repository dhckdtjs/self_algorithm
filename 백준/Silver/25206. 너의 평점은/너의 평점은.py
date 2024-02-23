# 너의 평점은
grade_list = []
grade_dict = {'A+':4.5,
              'A0':4.0,
              'B+':3.5,
              'B0':3.0,
              'C+':2.5,
              'C0':2.0,
              'D+':1.5,
              'D0':1.0,
              'F':0.0
}
s = 0
num_s = 0
for i in range(20):
    exam,num,grade = map(str,input().split())
    if grade in grade_dict:
        num_s+=float(num)
        total = float(num)*grade_dict[grade]
        grade_list.append(total)
        


for i in range(len(grade_list)):
    s+=grade_list[i]
print(s/num_s)