import datetime


now  = datetime.datetime.now()

print(now)

print(now.year)
print(now.month)
print(now.day)
print(now.hour)
print(now.minute)
print(now.second)
print(now.microsecond)

birthday = datetime.date(20,2,24)
print(f"birthday month is {birthday.month}, and the day is {birthday.day}" )
