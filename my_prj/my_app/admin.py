from django.contrib import admin

# Register your models here.

from .models import Article, Site

admin.site.register(Article)
admin.site.register(Site)