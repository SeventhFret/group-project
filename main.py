from os import system
from datetime import datetime, timedelta
import pyjokes
import calendar


date = datetime.utcnow()
utc_time = calendar.timegm(date.utctimetuple())
print("Current time in UNIX format is: ", utc_time)