import datetime

current_time = datetime.datetime.now()
print(current_time)
print(type(current_time))

current_time = datetime.datetime.strftime(current_time,"%Y-%m-%d %H:%M:%S")
print(current_time)
print(type(current_time))
