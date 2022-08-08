import datetime as dt

time_now = dt.datetime.now()
time_year = time_now.year
time_month = time_now.month
time_day_of_week = time_now.weekday()
print(time_day_of_week)

time_date_of_birth = dt.datetime(year=2003, month=3, day=15, hour=10)
print(time_date_of_birth)