from django.contrib import admin
from manage.models import Department

class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('title',)


admin.site.register(Department, DepartmentAdmin)