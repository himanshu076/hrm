from django.contrib import admin
from . models import User, Department, Employee, Leave, Recruitment

# Register your models here.
admin.site.register(User)
admin.site.register(Department)
admin.site.register(Employee)
admin.site.register(Leave)
admin.site.register(Recruitment)

