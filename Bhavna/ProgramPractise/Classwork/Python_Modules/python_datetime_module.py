# 04/07/2025 Session Continue

from datetime import datetime, timedelta

print("Get current date with time:",datetime.now())
# Get current date with time: 2025-07-06 15:34:28.184905
print("Get today day:", datetime.now().day)
# Get today day: 6
print("Get today month:", datetime.now().month)
# Get today month: 7
print("Get today year:", datetime.now().year)
# Get today year: 2025

print(dir(datetime.now()))
print("get today date:",datetime.now().date())
# get today date: 2025-07-06
print("get current hour:",datetime.now().hour)
# get current hour: 15
print("get current min:",datetime.now().minute)
# get current min: 41

# "Return day of the week, where Monday == 0 ... Sunday == 6."
print(datetime.now().weekday()) # 6 = Sunday

# generate a variable with unique value
result = datetime.now().strftime("%d_%h_%Y_%H_%M_%S")
print("Result:",result)
# Result: 06_Jul_2025_15_45_10

# get next two days date
Output = datetime.now() + timedelta(days=2)
print(Output.date())
# 2025-07-08

# Get date of previous two days
output_date = datetime.now() - timedelta(days=2)
print(output_date.date()) # # 2025-07-04
print(output_date.date().strftime("%d_%h_%Y"))
# 04_Jul_2025

# Get current time zoone name
print(datetime.now().astimezone().tzname())
# India Standard Time