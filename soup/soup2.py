from datetime import datetime, timedelta

# open a file which contains a text representation of a DOM which is to be examined.
# note that the source document is of no use, it has to be the text representation of the dom
# this is available from the developer console in chrome
f = open('soup/fenland.txt')
html_doc = f.read()


# define some lists

# links contains a tags which have links to meeting info
links = []
meetingStartTime = []
meetingDuration = []
days = []
meetingName = []
meetingTime = []
meetingAddress = []
meetingPostCode = []
#address is meetingAddress parsed into seperate lines
address = []
latitude = []
longtitude = []

from bs4 import BeautifulSoup

soup = BeautifulSoup(html_doc, 'html.parser')

"""
from the h3 tags build a list of meeting names
"""

for tag in soup.find_all('h3'):
    # h3 tags contain an inner image tag, so the following to get to the string info
    for string in tag.strings:
        print(repr(string))
        meetingName.append(repr(string))
    #print(tag.string)

"""
from the div tags build lists for day, time, and post code
"""

for tag in soup.find_all('div'):
    #print(tag.string)
    try:
        #print (tag['class'])
        if tag['class'] == ["day"]:
            print (tag.string)
            days.append(tag.string)
            meetingAddress.append(tag.next_sibling.next_sibling.string)
        if tag["class"]==['time']:
            for string in tag.stripped_strings:
                if string != "Time:":
				    #print(repr(string))
                    txt = repr(string)
                    x = txt.split()
					#hjhjhjhjhj
                    meetingTime.append(string)
        if tag["class"]==['postcode']:
            for string in tag.strings:
                if string != "Postcode:":
                    meetingPostCode.append(repr(string))
        

    except:
        print("error!")

"""
from the a tags derive latitude  and lontitude info
"""
for link in soup.find_all('a'):
	string = link.get("href")
	#print(string)
	if str(string).find("javascript:showMeetingInfo") != -1: links.append(string)

for link in links:
	#if link.href[0:25] == 'javascript:showMeetingInfo':
	link = link.split(",")

	lat = link[2].strip(",')")
	long = link[3].strip(",')")
	latitude.append(float(lat))
	longtitude.append(float(long))
	print(link[2].strip(",')"))
	print(link[3].strip(",')"))



"""
 parse meeting time into starttime and duratioon
 """
for myTime in meetingTime:
	# meeting start time
	meetingStartTime.append(myTime[0:5].replace(".", ":"))
	ixh = myTime.find('hr')
	if ixh != -1:
		h = int(myTime[ixh-1])
	else:
		h = 0
	ixm = myTime.find('mins')
	if ixm != -1:

		m = int(myTime[ixh+3:ixh+5])
		#print(m, myTime, ixh)
	else:
		m = 0
	# meeting end time
	meetingDuration.append(timedelta(hours=h, minutes = m))

for item in  meetingAddress:
	item = item.lstrip("' ")
	#creates a list
	item = item.rsplit(",")
	address.append(item)

#spacer = '##################################'
# print(spacer)
# print(days)
# print(spacer)
# print(meetingName)
# print(spacer)
# print(meetingStartTime)
# print(spacer)
# print(meetingDuration)
# print(spacer)
# print(meetingAddress)
# print(spacer)
# print(meetingPostCode)
# print(spacer)
# print(len(days))
# print(len(meetingName))
# print(len(meetingTime))
# print(len(meetingAddress))
# print(len(meetingPostCode))
# print(spacer)

for i in range(65):
	try:
		address[i][1]
	except:
		address[i].append("")
	try:
		address[i][2]
	except:
		address[i].append("")


#print(address[2])
""" now we have all the data we can add it to the database

to run this from django shell

>>> exec(open('soup/soup2.py').read())

"""

# import the models
from wtf.models import Region, Ig, Group, Venue, Meeting

# get the Ig 
ig = Ig.objects.get(pk=1)

for ix in range(65):
	# add the group and save it in g
	g = Group(name = meetingName[ix], ig = ig)
	g.save()

	# add the venue and saave it in v
	v = Venue(
		name = meetingName[ix],
		address1 = address[0], 
		address2 = address[1],
		address3 = address[2],
		postcode = meetingPostCode[ix],
		latitude = latitude[ix],
		longitude = longtitude[ix],
		disabledAccess = True
	)
	v.save()
	# now you can add the meeting
	m = Meeting(
		group = g,
		venue = v,
		day = days[ix],
		startTime = meetingStartTime[ix],
		duration = meetingDuration[ix],
		description = ""
	)



# add the meeting using g and v as the foreign key fields





#iterate
