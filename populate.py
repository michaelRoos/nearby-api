from mainview.models import categories
from mainview.models import event
import random

events = {"Hub Carnival": "Spring festival on the hub lawn with inflatables and food.",
          "Basketball Game": "Come support penn state basketball against Michigan at 7:00PM.",
          "Free Pizza With SPA!": "Celebrate the coming of spring with free pizza on the hub lawn. Now until 4PM.",
          "Resume Review": "Come get your resume reviewed by advising experts in preparation for the career fair.",
          "NERF War": "Unleash your inner child in an all out NERF war.",
          "Concert: Nickelback": "Come jam to some tunes!",
          "Girl Scout Cookies": "Saw the stand on the way to class, who doesn't love girl scout cookies?",
          "PSU Talent Show": "Watch your fellow students do amazing things.",
          "Pickup Soccer": "Playing with a couple friends, drop by if you want to join!",
          "Fun Run": "A casual 30-mile run, open to all. Starts at 5pm!",
          "Pie a professor": "Our entrepreneurship professor is letting people pay to pie him in the face!",
          "Arts and Crafts": "Show your creative side! We have paper, coloring utensils, and more!",
          "Speed Dating": "Meet your soul mate. Sponsored by PSU Singles.",
          "Saquon Sighting!": "Was walking by and saw Saquon recording an interview!!!",
          "Tightrope Exhibition": "Watch incredible displays of balance and athleticism. Sponsored by the PSU Tightrope Club",
          "Model Rocket Launch": "Come watch our live fire test of a model rocket! Completely safe!!! Sponsored by Lunar Lion."}

emails = ["coolguy19@gmail.com",
          "oldman55@aol.com",
          "billgates@microsoft.com",
          "markzucc@facebook.com",
          "lpage@google.com",
          "satya@microsoft.com",
          "spichai@google.com",
          "mdell@dell.com",
          "ebarron@psu.edu",
          "kanye@me.com",
          "rocket@psu.edu",
          "wul2@psu.edu"]

names = ["Ngoc",
         "Alphonso",
         "Margarito",
         "Miesha",
         "Cassi",
         "Bernetta",
         "Madge",
         "Renna",
         "Lemuel",
         "Donya",
         "Karina",
         "Cherly",
         "Bernardine",
         "Freda",
         "Olevia",
         "Ronny",
         "Mayola",
         "Avis",
         "Ashlie",
         "Orville"]
comments = ["We are!",
            "So much fun!",
            "Not a fan, personally",
            "PSU rocks!",
            "Wish they had puppies",
            "10/10 event",
            "Wish this hadn't happened",
            "I saw President Barron, but that's about it",
            "Meh",
            "Can't wait for this to happen again",
            "So exciting!",
            "Omg I loved this",
            "Great!!!",
            "Really well done, looking forward to the next one"]

keys = list(events.keys())
categories.objects.all().delete()
event.objects.all().delete()

all = categories()
all.title = "All"
all.save()

list = ["Athletics", "Food", "Animals", "Fundraiser", "Professional", "Music"]
level1 = []

for title in list:
    temp = categories()
    temp.title = title
    temp.parent = all
    temp.save()
    level1.append(temp)

list = [
    ['Clubs', 'Varsity', 'Football', 'Soccer', 'Hockey', 'Volleyball', 'Basketball'],
    ['Pizza', 'Dessert', 'Vegan', 'Vegetarian'],
    ['Dogs', 'Cats'],
    ['Charity', 'Club', 'Nonprofit'],
    ['Information', 'Career Fair', 'Development', 'Resume Review', 'Interview Prep'],
    ['Concerts', 'Street Performance', 'Alternative', 'Classic', 'Rock', 'Pop', 'Hip-Hop/Rap']
]
for i in range(len(level1)):
    parent = level1[i]
    children = list[i]
    for title in children:
        temp = categories()
        temp.title = title
        temp.parent = parent
        temp.save()

for i in range(16):
    temp_event = event()
    temp_event.title = keys[i]
    temp_event.description = events[temp_event.title]
    temp_event.lat = str(random.uniform(40.79, 40.81))[:10]
    temp_event.long = str(random.uniform(-77.87, -77.85))[:10]
    temp_event.planned_event = False
    temp_event.zipcode = 16802
    if temp_event.title == "Saquon Sighting!":
        temp_event.user_email = "recruiting@clevelandbrowns.com"
    else:
        temp_event.user_email = random.choice(emails)
    temp_event.comments = {random.choice(names): random.choice(comments)}
    temp_event.upvote_count = random.randint(10, 1000)
    temp_event.save()
    temp_event.categories.add(categories.objects.all().filter(title__icontains='All')[0])
    temp_event.categories.add(random.choice(categories.objects.all()))
    temp_event.save()
#
# temp_event = event()
# temp_event.title = "Hub Carnival"
# temp_event.description = 'Spring festival on the hub lawn with inflatables and food.'
# temp_event.lat = '40.797938'
# temp_event.long = '-77.860283'
# temp_event.planned_event = False
# temp_event.zipcode = 18601
# temp_event.user_email = "abc0@psu.edu"
# temp_event.comments = {"Michael": "This was fun"}
# temp_event.upvote_count = 0
# temp_event.save()
# temp_event.categories.add(categories.objects.all().filter(title__icontains='All')[0])
# temp_event.categories.add(categories.objects.all().filter(title__icontains='Food')[0])
# temp_event.save()
#
# temp_event = event()
# temp_event.title = "Basketball Game"
# temp_event.description = 'Come support penn state basketball against Michigan at 7:00PM.'
# temp_event.lat = '40.797938'
# temp_event.long = '-77.860283'
# temp_event.planned_event = False
# temp_event.zipcode = 18601
# temp_event.user_email = "abc0@psu.edu"
# temp_event.comments = {"Michael": "Great Game"}
# temp_event.upvote_count = 0
# temp_event.save()
# temp_event.categories.add(categories.objects.all().filter(title__icontains='All')[0])
# temp_event.categories.add(categories.objects.all().filter(title__icontains='Athl')[0])
# temp_event.categories.add(categories.objects.all().filter(title__icontains='Bask')[0])
# temp_event.save()
#
# temp_event = event()
# temp_event.title = "Free Pizza With SPA"
# temp_event.description = 'Celebrate the coming of spring with free pizza on the hub lawn. Now until 4PM.'
# temp_event.lat = '40.797938'
# temp_event.long = '-77.860283'
# temp_event.planned_event = False
# temp_event.zipcode = 18601
# temp_event.user_email = "abc1@psu.edu"
# temp_event.comments = {"Michael": "This was fun"}
# temp_event.upvote_count = 0
# temp_event.save()
# temp_event.categories.add(categories.objects.all().filter(title__icontains='All')[0])
# temp_event.categories.add(categories.objects.all().filter(title__icontains='Food')[0])
# temp_event.save()
#
# temp_event = event()
# temp_event.title = "Resume Review"
# temp_event.description = 'Come get your resume reviewed by advising experts in preparation for the career fair.'
# temp_event.lat = '40.797938'
# temp_event.long = '-77.860283'
# temp_event.planned_event = False
# temp_event.zipcode = 18601
# temp_event.user_email = "abc2@psu.edu"
# temp_event.comments = {"Michael": "Very Helpful", "Arjun": "I learned a lot"}
# temp_event.upvote_count = 0
# temp_event.save()
# temp_event.categories.add(categories.objects.all().filter(title__icontains='All')[0])
# temp_event.categories.add(categories.objects.all().filter(title__icontains='Athl')[0])
# temp_event.categories.add(categories.objects.all().filter(title__icontains='Bask')[0])
# temp_event.save()
