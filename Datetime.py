# Date time module  in python....
import datetime
import calendar
x=datetime.datetime.now()
y=x.strftime("%M") # week day shows %a tue %A
z=x.strftime(" %S ")
a=x.strftime("%b") # shows the name of the month 
year=x.strftime("%Y") # show the year name

print(x)
print(z)
print(a)
print(year)

cal=calendar.month(1989,8)
print(cal)












import time
local_time=time.localtime(time.time())
local_time1=time.asctime(time.localtime(time.time())) # asctime provides us to read in human readable form...
print(local_time)
print(local_time1)
