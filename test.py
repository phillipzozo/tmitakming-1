
from datetime import datetime, timezone, timedelta
dt = datetime.utcnow()
print(dt)
dt = dt.replace(tzinfo=timezone.utc)
print(dt)
tzutc_8 = timezone(timedelta(hours=8))
local_dt = dt.astimezone(tzutc_8)
print(local_dt)
