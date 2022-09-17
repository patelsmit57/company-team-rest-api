from django.contrib import admin
from .models import *
# Register your models here.

class CompanyAdmin(admin.ModelAdmin):
    list_display =['UUID','name', 'CEO', 'Inception_date']


class TeamAdmin(admin.ModelAdmin):
    list_display =['UUID','CompanyID', 'Lead_Name']


admin.site.register(Company, CompanyAdmin)
admin.site.register(Team, TeamAdmin)