import datetime
import schedule
import time
def job():
    a = datetime.datetime.today()
    o = datetime.timedelta(hours=8)
    print((a+o).strftime("%Y-%m-%d_%H:%M:%S"))
    if int((a+o).strftime("%S")) == 0:
        print((a+o).strftime("%Y-%m-%d_%H:%M:%S"))


schedule.every().second.do(job)

while True:
    schedule.run_pending()
    time.sleep(1)
