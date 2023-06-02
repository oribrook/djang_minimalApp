from django.contrib import admin

# Register your models here.

from .models import Person, Car, Rent

admin.site.register(Person)
admin.site.register(Car)
admin.site.register(Rent)