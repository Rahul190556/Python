from datetime import date

# calling the today
# function of date class
today = date.today()

print("Today's date is", today)


from datetime import datetime

yesterday = datetime(2023, 5, 23, 13, 0, 0, 0)
now = datetime.today()
delta = now - yesterday
print(delta.days)
print(str(delta))
