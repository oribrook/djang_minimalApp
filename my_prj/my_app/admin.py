from django.contrib import admin

# Register your models here.

from .models import Person, Car, Rent
from django.contrib.sessions.models import Session

admin.site.register(Person)
admin.site.register(Car)
admin.site.register(Rent)
admin.site.register(Session)