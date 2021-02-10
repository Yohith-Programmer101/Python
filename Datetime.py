import datetime as dt
import pytz

today = dt.date.today()
print(today)

birthday = dt.date(2008, 10, 6)
print(birthday)

days_since_birth = (today - birthday).days
print(days_since_birth)

tdelta = dt.timedelta(days=10)
print(today - tdelta)

print(today.day)
print(today.weekday()) # for this it is monday: 0, sunday: 6
print(today.year)

print(dt.time(7, 23, 45, 112345))
# dt.date(y, m, d)
# dt.time(hr, min, sec, milsec)
# dt.datetime(y, m, d, hr, min, sec, milsec)

hour_delta = dt.timedelta(hours=10)
print(dt.datetime.now())
print(dt.datetime.now() + hour_delta)

datetime_today = dt.datetime.now(tz=pytz.UTC)
datetime_india = datetime_today.astimezone(pytz.timezone("Indian/Christmas"))
print(datetime_today)
print(datetime_india)

for i in pytz.all_timezones: # returns all time zones
    print(i)

# string formatting with dates
# 2020-10-03 -> October 06, 2020
# strftime (f - formatting)
print(datetime_india.strftime("%B %d, %Y")) # %B -> month, %d -> day, %y -> year

# October -> datetime(2020, 10, 3)
# strptime (p - parsing)
datetime_thing = dt.datetime.strptime("October 06, 2020", "%B %d, %Y")
print(datetime_thing)