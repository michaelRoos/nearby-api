from django.contrib import admin
from django.contrib.auth.models import User

from .models import event
from .models import *

# Register your models here.
admin.site.register(event)
admin.site.register(upvotes)
admin.site.register(categories)
admin.site.register(file)