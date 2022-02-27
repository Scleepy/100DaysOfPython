def is_leap(year):  
    if year % 4 != 0:
        return False
    else:
        if year % 100 != 0:
            return True
        else:
            if year % 400 == 0:
                return True
            else:
                return False

def get_days(year, month):
    days_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    if month == 2 and is_leap(year):
        return 29
    else:
        return days_month[month-1]
        
year = int(input("Enter a year: "))
month = int(input("Enter a month: "))

print(get_days(year, month))