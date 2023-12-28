# admin.py in your app
from django.contrib import admin
from .models import *

admin.site.register(Admin)
admin.site.register(positions)

