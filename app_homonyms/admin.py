from django.contrib import admin

# Register your models here.
from .models import WordType, Homonyms

admin.site.register(WordType)
admin.site.register(Homonyms)
