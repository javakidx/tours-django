import os
import django
import random

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tours_django.settings')
django.setup()

# This import cannot be at the top or error will be thrown
from tours_app.models import AccessRecord, Topic, Webpage, User
from faker import Faker

faker_gen = Faker()
topics = ['Search', 'Social', 'Marketplace', 'News', 'Games']


def add_topic():
    t = Topic.objects.get_or_create(top_name=random.choice(topics))[0]
    t.save()
    return t


def populate(N=5):
    for entry in range(N):
        top = add_topic()

        fake_url = faker_gen.url()
        fake_date = faker_gen.date()
        fake_name = faker_gen.company()

        web_page = Webpage.objects.get_or_create(topic=top, url=fake_url, name=fake_name)[0]

        acc_rec = AccessRecord.objects.get_or_create(name=web_page, date=fake_date)[0]


def populate_user(n=5):
    for i in range(n):
        u = User.objects.get_or_create(first_name=faker_gen.first_name(), last_name=faker_gen.last_name(),
                                       email=faker_gen.email())[0]
        u.save()


if __name__ == '__main__':
    print('Population started')
    # populate(20)
    populate_user(20)
    print('Population complete')
