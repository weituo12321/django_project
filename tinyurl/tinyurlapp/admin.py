from django.contrib import admin
from .models import Musician, Album

# Register your models here.
@admin.register(Musician, Album)
class Musicadmin(admin.ModelAdmin):
    pass


