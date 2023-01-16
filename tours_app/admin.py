from django.contrib import admin
from tours_app.models import AccessRecord, Topic, Webpage, User, UserProfileInfo, School, Student

# Register your models here.
admin.site.register(AccessRecord)
admin.site.register(Topic)
admin.site.register(Webpage)
admin.site.register(User)
admin.site.register(UserProfileInfo)
admin.site.register(School)
admin.site.register(Student)
