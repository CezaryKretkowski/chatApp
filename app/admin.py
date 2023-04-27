from django.contrib import admin
from django.contrib.auth.models import Group
from .models import *

admin.site.unregister(Group)
admin.site.register(Message)
admin.site.register(Profile)
admin.site.register(Room)
