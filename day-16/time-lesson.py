import time

print(time.ctime(0))
print(time.time())
print(time.ctime(time.time()))

time_obj = time.localtime()
print(time_obj.tm_mon)

print(time.strftime('%B %d %Y %H:%M:%S', time_obj))


time_str = '20 April, 2020'
time_obj = time.strptime(time_str, '%d %B, %Y')
print(time_obj)
time_tuple = (2020, 4, 20, 4, 20, 0, 0, 0, 0)
time_str = time.asctime(time_tuple)
print(time_str)