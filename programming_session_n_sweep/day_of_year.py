"""


You’re given a date string in the format month/day/year, based on the Gregorian calendar.
Your task is to return which day of the year that date corresponds to (1–365, or 1–366 for leap years).
https://en.wikipedia.org/wiki/Gregorian_calendar

"""



def dayOfYear(date):

    # separate the string data
    # month = date.split('/')[0]
    # day = date.split('/')[1]
    # year = date.split('/')[2]
    month, day, year = [int(i) for i in date.split("/")]
    
    # day in each month 
    days = [31,28, 31, 30, 31, 30, 31, 31, 30, 31, 30 ,31]
    
    
    #leap year logic 
    
    #if it is a leap year 
    
    div4 = year % 4 == 0 # leap year
    div100 = year % 100 == 0 # no leap year
    div400 = year % 400 == 0 # leap year 
    
    #leap year
    if (div4 and not div100) or div400:
        days[1] =29
        
    print(sum(days[:month-1]) + day)
        

dayOfYear("12/13/2020")
# output = 348

dayOfYear("11/16/2020")
# output = 321

dayOfYear("1/9/2019")
# output = 9

dayOfYear("3/1/2004")
# output = 61

dayOfYear("12/31/2000")
# output = 366 # leap year
dayOfYear("12/31/2019")
# output = 365 #non leap year


dayOfYear("12/31/1900")

