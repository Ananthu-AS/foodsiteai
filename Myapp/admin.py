from django.contrib import admin

# Register your models here.
from .models import Foodtype, Meals, variety
admin.site.register(variety)
admin.site.register(Foodtype)
admin.site.register(Meals)
