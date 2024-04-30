from datetime import datetime
import math
# Get the current day, month, year, hour, minute and timestamp from datetime module
# It really seems that there should've been an f string tutorial somewhere....

now = datetime.now()
print((f'Current day: {now.day} \nCurrent month: {now.month}\nCurrent year: {now.year}\n'
      f'Current hour: {now.hour}\nTimestamp: {now.timestamp()}'))


time = now.strftime("%d/%m/%Y, %H:%M:%S")
print("time two: ", time)


date_string = "5 December, 2019"
print("date_string =", date_string)
date_object = datetime.strptime(date_string, "%d %B, %Y")
print("date_object =", date_object)

def calculate_time_since(time_str):
      # st = "1 January 2025"
      now = datetime.now()
      past_year = False # if this is false then we are calculating time until
      months = {1:31,2:28,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}
      
      months_long = {"january":1,"february":2,"march":3,"april":4,"may":5,"june":6,"july":7,"august":8,"september":9,"october":10,"november":11,"december":12}
      
      if any(string in time_str.lower() for string in months_long.keys()):
            time_str = datetime.strptime(time_str, "%d %B %Y")
      else:      
            time_str = datetime.strptime(time_str, "%d %m %Y")
      # 2025 < 2024
      if time_str.year < now.year:
            past_year = True
      if time_str.month < now.month and time_str.year < now.year:
            past_year = True
      if time_str.day < now.day and time_str.month < now.month and time_str.year < now.year:
            past_year = True
      
      print("Input value: ", time_str)
      print("Current value: ", now)
      
      if past_year == False:
            years_past = time_str.year - now.year - 1 
            months_past = 12-now.month + time_str.month - 1
            days_past = months[int(now.month)] - now.day + time_str.day
            leap_years = math.floor(int(time_str.year)/int(now.year))
      else:
            years_past = now.year - time_str.year - 1
            months_past = 12 - time_str.month + now.month - 1
            days_past = months[int(time_str.month)] - time_str.day + now.day
            leap_years = math.floor(int(now.year)/int(time_str.year))
      
      days_past += leap_years
      
      return ({"years":years_past,"months":months_past,"days":days_past})

print(calculate_time_since("1 January 2025"))