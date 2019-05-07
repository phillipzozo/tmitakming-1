import datetime
a = datetime.datetime.today()

o = datetime.timedelta(hours=8)
print((a+o).strftime("%Y-%m-%d_%H:%M"))
