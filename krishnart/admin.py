from django.contrib import admin

# Register your models here.

from .models import Drawings as drawing

class DrawingDB(admin.ModelAdmin):
    list_display = ('name', 'caption', 'image', 'date')

admin.site.register(drawing, DrawingDB)