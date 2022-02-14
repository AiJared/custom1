from django.contrib import admin
from Accounts.models import User, Teacher, Student

admin.site.register(User)
admin.site.register(Student)
admin.site.register(Teacher)