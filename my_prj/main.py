import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "my_prj.settings")


import django
django.setup()


# here you can use all django models/features etc


# from my_app.models import *
from django.contrib.auth.models import User
users = User.objects.all()
[print(u.username) for u in users]
# ...
