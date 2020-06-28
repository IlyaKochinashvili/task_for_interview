from django.contrib import admin

from department.models import Department, User


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    pass


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    pass

