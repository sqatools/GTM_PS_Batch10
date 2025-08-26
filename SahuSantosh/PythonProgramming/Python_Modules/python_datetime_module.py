from datetime import datetime, timedelta

print("get current date with time :", datetime.now()) # 2025-07-04 19:24:12.601950
print("get today day :", datetime.now().day) #  4
print("get current month:", datetime.now().month) # 7
print("get current Year", datetime.now().year) # 2025
print(dir(datetime.now()))
print("get today date:", datetime.now().date()) # 2025-07-04
print("get current hour:", datetime.now().hour) #  19

# "Return day of the week, where Monday == 0 ... Sunday == 6."
print(datetime.now().weekday()) # 4 == Friday


# generate a variable with unique value
result = datetime.now().strftime("%d_%h_%Y_%H_%M_%S")
print("Result :", result) # 04_Jul_2025_19_32_43


# get next two days date
output = datetime.now() + timedelta(days=2)
print(output.date())  # 04_Jul_2025_19_32_43


# get two days previous date
output2 = datetime.now() - timedelta(days=2)
print(output2.date()) # 2025-07-02

# Get current time zone name.
print(datetime.now().astimezone().tzname()) # India Standard Time
