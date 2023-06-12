import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "my_prj.settings")


import django
django.setup()

# here you can use all django models/features etc


# from my_app.models import Note
from my_app.models import Note
import random
import string

def random_char(size):
    return ''.join(random.choice(string.ascii_letters + "  ") for x in range(size))


for i in range(1000):

    title = random_char(size=random.randint(4, 7))
    content = random_char(size=random.randint(15, 70))
    n = Note.objects.create(title=title, content=content)
    n.save()
    


    
