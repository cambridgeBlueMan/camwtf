""" from datetime import datetime, time

datetime_str = '19.15'

datetime_obj = time.strptime(datetime_str, '%H::%M::')
print(datetime_obj)
print(type(datetime_obj)) """


from datetime import datetime, timedelta

my_date_string = "11:31"
datetime_object = datetime.strptime(my_date_string, '%H:%M').time()

print(type(datetime_object))
print(datetime_object)

my_duration = '1hr 15mins'
myList = my_duration.split()
h = myList[0][0]
my_delta = timedelta(hours=int(myList[0][0]))
print(my_delta)