import datetime

x = datetime.datetime.now()
print(x)

print(datetime.datetime(2022,1,21))




print()
# get year %y for shortest or %Y for complete year like 2025
x = datetime.datetime.now()
m = x.strftime("%Y")
print(m)



print()
# get month %b for shortest or %B for complete
x = datetime.datetime.now()
m = x.strftime("%B")
print(m)



print()
# get month %m for month no or %M for mintues
x = datetime.datetime.now()
m = x.strftime("%M")
print(m)


