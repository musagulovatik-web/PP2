import datetime
x=datetime.datetime.now() #now
#1
y=x-datetime.timedelta(days=5)
print(y)
#2
z=x-datetime.timedelta(days=1) #yesterday
t=x+datetime.timedelta(days=1) #tomorrow
print(z, x, t) 
#3
u=x.strftime('%Y-%m-%d %H:%M:%S')#without microsec
print(u)
#4
l=(t-x).total_seconds() #difference in seconds
print(l) 