# timezone-aware scheduling system 
from datetime import datetime 
import pytz

# Event scheduled in new your time 
first_timezone = pytz.timezone ("America/new_york")
first_event = first_timezone.localize\
(datetime(2024, 8, 22, 15, 0, 0))

# convert to german time 
second_timezone = pytz.timezone("europe/berlin")
second_event = first_event.\
     astimezone(second_timezone)
   
#print(pytz.all_timezones)

# extract and display location names 
# from timezone objects
first_location = first_timezone.zone
second_location = second_timezone.zone

# display times 
print(f"time at {first_location}:{first_event}")
print(f"time at {second_location}:{second_event}")
