from django.contrib import admin
from .models import event
from .models import *

# Register your models here.
admin.site.register(event)
admin.site.register(users)
admin.site.register(zip_location)
admin.site.register(images)
admin.site.register(times)
admin.site.register(upvotes)
admin.site.register(categories)
admin.site.register(event_categories)
