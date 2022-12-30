import csv  # https://docs.python.org/3/library/csv.html

# https://django-extensions.readthedocs.io/en/latest/runscript.html

# python3 manage.py runscript add_latlong_to_towns

from wtf.models import Town

def run():
    towns = Town.objects.filter(county_id=5 )
    print(towns)

    counter = 0 
    for town in towns:
        print(town.name)
    for town in towns:
        # find the town in the psotcodes file
        #print(town.name)
        fhand = open('soup/postcodes.csv')
        reader = csv.reader(fhand)
        for row in reader:
            # print(row)
            if town.name == row[5] or town.name == row[6]:
                town.latitude=row[3]
                town.longtitude = row[4]
                print(row[5])
                print(town.name)
                counter = counter +1

                town.save()
    print("records found:", counter)
