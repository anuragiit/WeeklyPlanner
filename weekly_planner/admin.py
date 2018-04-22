from django.contrib import admin

# Register your models here.

from .models import toDoList

class toDoListadmin(admin.ModelAdmin):
    list_display=["userdetails","taskName","description","status","ts"]

admin.site.register(toDoList,toDoListadmin)