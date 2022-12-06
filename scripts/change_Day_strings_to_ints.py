# import csv  # https://docs.python.org/3/library/csv.html

# https://django-extensions.readthedocs.io/en/latest/runscript.html

# python3 manage.py runscript scripts/change_Day_strings_to_ints.py

def run():
    from wtf.models import Meeting

    meetings = Meeting.objects.all()

    for meeting in meetings:
        if meeting.day == "Sunday":
            meeting.dayAsInt = 1
            meeting.save()
        if meeting.day == "Monday":
            meeting.dayAsInt = 2
            meeting.save()
        if meeting.day == "Tuesday":
            meeting.dayAsInt = 3
            meeting.save()
        if meeting.day == "Wednesday":
            meeting.dayAsInt = 4
            meeting.save()
        if meeting.day == "Thursday":
            meeting.dayAsInt = 5
            meeting.save()
        if meeting.day == "Friday":
            meeting.dayAsInt = 6
            meeting.save()
        if meeting.day == "Saturday":
            meeting.dayAsInt = 7
            meeting.save()


# def run():
#     fhand = open('soup/Towns_List.csv')
#     reader = csv.reader(fhand)
#     next(reader)  # Advance past the header

#     County.objects.all().delete()
#     Town.objects.all().delete()

#     # Name,Breed,Weight
#     # Abby,Sphinx,6.4
#     # Annie,Burmese,7.6
#     # Ash,Manx,7.8
#     # Athena,Manx,8.9
#     # Baby,Tabby,6.9


#     #town, county, country

#     for row in reader:
#         print(row)

#         c, created = County.objects.get_or_create(name=row[1], country = row[2])

#         t = Town(county=c, name=row[0])
#         t.save()
