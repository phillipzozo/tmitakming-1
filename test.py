import pytz
import datetime
zh = (pytz.country_timezones('tw'))
n = datetime.datetime.now(zh)
print(n)