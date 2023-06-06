import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "my_prj.settings")


import django
django.setup()


from my_app.models import Car, Person

from django.db import connection

with connection.cursor() as curser:

    query = "select car_type from my_app_car where car_type like %s"
    curser.execute(query, ['Toyota'])
    # res = curser.fetchmany(5)
    # for item in curser:
    #     print(item)
    # first = curser.fetchone()
    # second = curser.fetchone()

    # print(first)
    # print(second)
    print(curser.fetchone())
    print(res)

exit()
    


# Car.objects.raw("select ...")




# print(list(Car.objects.all()))

# csv_file = r"C:\Users\jbt\Desktop\fsori\DMA\cars.csv"
# with open(csv_file, 'r') as FH:
#     lines = FH.readlines()

# lines = lines[1:]    
# cars = [l.replace("\n", "") for l in lines]

# p = Person.objects.first()
# for l in cars:
#     l = l.split(",")    
#     Car.objects.create(car_type=l[1], cost=int(l[6]), year=int(l[2]), owner=p)


from django.db.transaction import atomic


# try:
#     with atomic():    
#         Car.objects.create(car_type="unknown", cost=400, year=3000, owner=p)
#         import time
#         time.sleep(200)
#         Person.objects.create(x=5)
# except Exception as e:
#     # return Ht
#     pass


cars = Car.objects.all()
print(cars[0])
print(cars[1])
# for c in cars:
#     print(c.car_type)


