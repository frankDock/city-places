import os
import sys

proj_path = os.curdir
# This is so Django knows where to find stuff.
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "elleday.settings")
sys.path.append(proj_path)

# This is so my local_settings.py gets loaded.
os.chdir(proj_path)

# This is so models get loaded.
from django.core.wsgi import get_wsgi_application
from django.db.utils import IntegrityError

application = get_wsgi_application()

from places.models import Place, Category, Tag
import csv

r = csv.reader(open('data.csv'))
r.next()
for row in r:
    try:
        place = Place()
        place.title = row[0]
        place.address = row[8]
        if len(row[9]) < 32:
            place.phone = row[9]
        else:
            place.phone = ""
        place.budget = row[10]
        place.style = row[11]
        place.adventure = row[12]
        place.landscape = row[13]
        place.must_see = row[14]
        place.energy = row[15]
        place.save()

        for x in range(1, 4):
            try:
                category = Category.objects.filter(name=row[x]).first()
                if not category:
                    category = Category()
                    category.name = row[x]
                    category.save()
                    place.categories.add(category)
                    print category.name
                else:
                    place.categories.add(category)
                    print category.name
            except:
                pass

        for x in range(4, 8):
            try:
                tag = Tag(name=row[x])
                tag.save()
                place.tags.add(tag)
                print tag.name
            except:
                pass

        place.save()
        print place.title

    except ValueError:
        pass
    except IndexError:
        pass
