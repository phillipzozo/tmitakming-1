import datetime
import schedule
import time
import threading
def job():
    a = datetime.datetime.today()
    o = datetime.timedelta(hours=8)
    print((a+o).strftime("%Y-%m-%d_%H:%M:%S"))
    #if int((a+o).strftime("%S")) == 0:
     #   print((a+o).strftime("%Y-%m-%d_%H:%M:%S"))
    timer = threading.Timer(5, job)
    timer.start()

schedule.every().second.do(job)

#while True:
 #   schedule.run_pending()
 #   time.sleep(1)


def printHello():
    print ("Hello World")
    global timer
    #timer = threading.Timer(5.5, job)
    #timer.start()

if __name__ == "__main__":
    printHello()
    timer = threading.Timer(1, job)
    timer.start()

