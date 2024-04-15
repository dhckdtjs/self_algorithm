while True:
    name,age,weight = input().split()
    if (name,age,weight) == ('#','0','0'):
        break
    elif int(age)<=17 and int(weight)<80:
        print(f'{name} Junior')
    else:
        print(f'{name} Senior')