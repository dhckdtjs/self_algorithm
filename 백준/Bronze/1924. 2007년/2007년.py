# 2007년
month,date = list(map(int,input().split()))
if month ==1 or month == 10:
    if date % 7 ==1:
        print('MON')
    elif date % 7 == 2:
        print("TUE")
    elif date % 7 == 3:
        print("WED")
    elif date % 7 == 4:
        print("THU")
    elif date % 7 == 5:
        print("FRI")
    elif date % 7 == 6:
        print("SAT")
    elif date % 7 == 0:
        print("SUN")
elif month == 2 or month == 3 or month == 11:
    if date % 7 ==1:
        print('THU')
    elif date % 7 == 2:
        print("FRI")
    elif date % 7 == 3:
        print("SAT")
    elif date % 7 == 4:
        print("SUN")
    elif date % 7 == 5:
        print("MON")
    elif date % 7 == 6:
        print("TUE")
    elif date % 7 == 0:
        print("WED")            
elif month == 4 or month == 7:
    if date % 7 ==1:
        print('SUN')
    elif date % 7 == 2:
        print("MON")
    elif date % 7 == 3:
        print("TUE")
    elif date % 7 == 4:
        print("WED")
    elif date % 7 == 5:
        print("THR")
    elif date % 7 == 6:
        print("FRI")
    elif date % 7 == 0:
        print("SAT")
elif month == 5:
    if date % 7 ==1:
        print('TUE')
    elif date % 7 == 2:
        print("WED")
    elif date % 7 == 3:
        print("THR")
    elif date % 7 == 4:
        print("FRI")
    elif date % 7 == 5:
        print("SAT")
    elif date % 7 == 6:
        print("SUN")
    elif date % 7 == 0:
        print("MON")
elif month == 6 :
    if date % 7 ==1:
        print('FRI')
    elif date % 7 == 2:
        print("SAT")
    elif date % 7 == 3:
        print("SUN")
    elif date % 7 == 4:
        print("MON")
    elif date % 7 == 5:
        print("TUE")
    elif date % 7 == 6:
        print("WED")
    elif date % 7 == 0:
        print("THR")   
elif month == 8:
    if date % 7 ==1:
        print('WED')
    elif date % 7 == 2:
        print("THR")
    elif date % 7 == 3:
        print("FRI")
    elif date % 7 == 4:
        print("SAT")
    elif date % 7 == 5:
        print("SUN")
    elif date % 7 == 6:
        print("MON")
    elif date % 7 == 0:
        print("TUE")   
elif month == 9 or month == 12:
    if date % 7 ==1:
        print('SAT')
    elif date % 7 == 2:
        print("SUN")
    elif date % 7 == 3:
        print("MON")
    elif date % 7 == 4:
        print("TUE")
    elif date % 7 == 5:
        print("WED")
    elif date % 7 == 6:
        print("THR")
    elif date % 7 == 0:
        print("FRI")      