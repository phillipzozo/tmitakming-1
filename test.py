import datetime
import schedule
import time
def job():
    a = datetime.datetime.today()
    o = datetime.timedelta(hours=8)
    print((a+o).strftime("%Y-%m-%d_%H:%M:%S"))


schedule.every(10).seconds.do(job)

while True:
    schedule.run_pending()
    time.sleep(1)
