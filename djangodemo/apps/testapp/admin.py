from django.contrib import admin

from .models import Employee
from .models import Team

admin.site.register(Employee)
admin.site.register(Team)
