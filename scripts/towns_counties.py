import csv  # https://docs.python.org/3/library/csv.html

# https://django-extensions.readthedocs.io/en/latest/runscript.html

# python3 manage.py runscript towns_counties

from wtf.models import County, Town

def run():
    fhand = open('soup/Towns_List.csv')
    reader = csv.reader(fhand)
    next(reader)  # Advance past the header

    County.objects.all().delete()
    Town.objects.all().delete()

    # Name,Breed,Weight
    # Abby,Sphinx,6.4
    # Annie,Burmese,7.6
    # Ash,Manx,7.8
    # Athena,Manx,8.9
    # Baby,Tabby,6.9


    #town, county, country

    for row in reader:
        print(row)

        c, created = County.objects.get_or_create(name=row[1], country = row[2])

        t = Town(county=c, name=row[0])
        t.save()
