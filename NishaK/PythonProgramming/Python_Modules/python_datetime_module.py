from datetime import datetime, timedelta


print("Current date with time :", datetime.now())
# Current date with time : 2025-07-06 12:12:34.881925

print("Today day :", datetime.now().day)
# Get today day : 6

print("Current Month :", datetime.now().month)
# Current Month : 7

print("Current Year :", datetime.now().year)
# Current Year : 2025

print("Today Date :", datetime.now().date())
# Today Date : 2025-07-06

print("Current Hour :", datetime.now().hour)
# Current Hour : 12

print(dir(datetime.now()))
# 'astimezone', 'combine', 'ctime', 'date', 'day', 'dst', 'fold', 'fromisocalendar',
# 'fromisoformat', 'fromordinal', 'fromtimestamp', 'hour', 'isocalendar', 'isoformat', 'isoweekday',
# 'max', 'microsecond', 'min', 'minute', 'month', 'now', 'replace', 'resolution', 'second',
# 'strftime', 'strptime', 'time', 'timestamp', 'timetuple', 'timetz', 'today', 'toordinal', 'tzinfo', 'tzname',
# 'utcfromtimestamp', 'utcnow', 'utcoffset', 'utctimetuple', 'weekday', 'year'


# "Return day of the week, where Monday == 0 ... Sunday == 6."
print(datetime.now().weekday())
# 6

# generate a variable with unique value
result = datetime.now().strftime("%d_%h_%Y_%H_%M_%S")
print("Result :", result)
# Result : 06_Jul_2025_12_22_51


# get next two days date
output = datetime.now() + timedelta(days=2)
print("Output :", output)
# Output : 2025-07-08 12:24:16.609807

# get two days previous date
output2 = datetime.now() - timedelta(days=2)
print("Output :", output2)
# Output : 2025-07-04 12:26:52.548117

# Get current time zone name.
print(datetime.now().astimezone().tzname())
# India Standard Time