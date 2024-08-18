from django.contrib import admin
from api.models import Company,Employee

class CompanyAdmin(admin.ModelAdmin):
    list_display=('name','location','type')
admin.site.register(Company,CompanyAdmin)
admin.site.register(Employee)