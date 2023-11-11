def is_leap_year(year_):
    if (year_ % 4 == 0 and year_ % 100 != 0) or (year_ % 400 == 0):
        return True
    else:
        return False


def days_in_month(year_, month_):
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if month_ == 2 and is_leap_year(year_):
        return 29
    else:
        return month_days[month_-1]


year = int(input("Enter a year: "))  # Enter a year
month = int(input("Enter a month: "))  # Enter a month
days = days_in_month(year, month)
print(days)


