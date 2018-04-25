from mainview.models import categories
from mainview.models import event


categories.objects.all().delete()
event.objects.all().delete()

all = categories()
all.title="All"
all.save()

list = ["Athletics", "Food", "Animals", "Fundraiser", "Professional", "Music"]
level1 = []

for title in list:
	temp = categories()
	temp.title = title
	temp.parent = all
	temp.save()
	level1.append(temp)

list =[
			['Clubs','Varsity','Football','Soccer','Hockey','Volleyball','Basketball'],
			['Pizza','Dessert','Vegan','Vegetarian'],
			['Dogs','Cats'],
			['Charity','Club','Nonprofit'],
			['Information','Career Fair','Development','Resume Review','Interview Prep'],
			['Concerts','Street Performance','Alternative','Classic','Rock','Pop','Hip-Hop/Rap']
		]
for i in range(len(level1)):
	parent = level1[i]
	children = list[i]
	for title in children:
		temp = categories()
		temp.title = title
		temp.parent = parent
		temp.save()







temp_event = event()
temp_event.title = "Hub Carnival"
temp_event.description = 'Spring festival on the hub lawn with inflatables and food.'
temp_event.lat = '40.797938'
temp_event.long = '-77.860283'
temp_event.planned_event = False
temp_event.zipcode = 18601
temp_event.user_email = "abc0@psu.edu"
temp_event.comments = {"Michael":"This was fun"}
temp_event.upvote_count = 0
temp_event.save()
temp_event.categories.add(categories.objects.all().filter(title__icontains='All')[0])
temp_event.categories.add(categories.objects.all().filter(title__icontains='Food')[0])
temp_event.save()



temp_event = event()
temp_event.title = "Basketball Game"
temp_event.description = 'Come support penn state basketball against Michigan at 7:00PM.'
temp_event.lat = '40.797938'
temp_event.long = '-77.860283'
temp_event.planned_event = False
temp_event.zipcode = 18601
temp_event.user_email = "abc0@psu.edu"
temp_event.comments = {"Michael":"Great Game"}
temp_event.upvote_count = 0
temp_event.save()
temp_event.categories.add(categories.objects.all().filter(title__icontains='All')[0])
temp_event.categories.add(categories.objects.all().filter(title__icontains='Athl')[0])
temp_event.categories.add(categories.objects.all().filter(title__icontains='Bask')[0])
temp_event.save()

temp_event = event()
temp_event.title = "Free Pizza With SPA"
temp_event.description = 'Celebrate the coming of spring with free pizza on the hub lawn. Now until 4PM.'
temp_event.lat = '40.797938'
temp_event.long = '-77.860283'
temp_event.planned_event = False
temp_event.zipcode = 18601
temp_event.user_email = "abc1@psu.edu"
temp_event.comments = {"Michael":"This was fun"}
temp_event.upvote_count = 0
temp_event.save()
temp_event.categories.add(categories.objects.all().filter(title__icontains='All')[0])
temp_event.categories.add(categories.objects.all().filter(title__icontains='Food')[0])
temp_event.save()

temp_event = event()
temp_event.title = "Resume Review"
temp_event.description = 'Come get your resume reviewed by advising experts in preparation for the career fair.'
temp_event.lat = '40.797938'
temp_event.long = '-77.860283'
temp_event.planned_event = False
temp_event.zipcode = 18601
temp_event.user_email = "abc2@psu.edu"
temp_event.comments = {"Michael":"Very Helpful","Arjun":"I learned a lot"}
temp_event.upvote_count = 0
temp_event.save()
temp_event.categories.add(categories.objects.all().filter(title__icontains='All')[0])
temp_event.categories.add(categories.objects.all().filter(title__icontains='Athl')[0])
temp_event.categories.add(categories.objects.all().filter(title__icontains='Bask')[0])
temp_event.save()



