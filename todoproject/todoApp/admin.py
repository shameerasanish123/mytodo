from django.contrib import admin
from . models import Register
from . models import Task
# Register your models here.
admin.site.register(Register)
admin.site.register(Task)