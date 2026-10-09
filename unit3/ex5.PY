import datetime

now = datetime.datetime.now()

print("Current date:", now.date())
print("Current time:", now.strftime("%H:%M:%S"))
print("Current date and time:", now)
