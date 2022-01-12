def is_leap(year):
    leap = False
    # divided by 100 means century year (ending with 00)
    # century year divided by 400 is leap year
    if (year % 400 == 0) and (year % 100 == 0):
        leap = True

    # not divided by 100 means not a century year
    # year divided by 4 is a leap year
    elif (year % 4 ==0) and (year % 100 != 0):
        leap = True

    # if not divided by both 400 (century year) and 4 
    #(not century year)
    # year is not leap year
    else:
        leap = False
    return leap

year = int(input())
print(is_leap(year))

'''
git add .
git commit -m 'Comments to be added'
git pull origin master
git push origin master

'''
