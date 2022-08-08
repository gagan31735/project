year = 2000
if (year % 400 == 0) and (year % 100 == 0):
    print(" 2000 is a leap year ".format(year))
elif (year % 4 == 0) and (year % 100 != 0):
    print(" 2000 is a leap year ".format(year))
else:
    print(" 2000 is not a leap year ".format(year))
