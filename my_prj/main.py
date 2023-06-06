import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "my_prj.settings")


import django
django.setup()


from my_app.models import Car

for i in range(10):
    Car.objects.create(car_type=f"toyota {i}", year=2000+i)


