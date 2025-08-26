from datetime import datetime,timedelta

print(datetime.now())
print(datetime.now().date())
print(datetime.now().day)
print(datetime.now().month)
print(datetime.now().year)
print(datetime.now().hour)
print(datetime.now().minute)
print(datetime.now().second)
print(datetime.now().weekday())

rst=datetime.now().strftime("%d_%B_%Y_%H_%M_%S_" "_%A" )
print(rst)

diff=datetime.now()-timedelta(days=2)
print(diff)

print(datetime.now().astimezone().tzname())