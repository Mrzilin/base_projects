from django.contrib import admin

# Register your models here.
from rbac.models import *


class UserProfileAdmin(admin.ModelAdmin):
    pass


admin.site.register(UserProfile, UserProfileAdmin)


class RoleAdmin(admin.ModelAdmin):
    pass


admin.site.register(Role, RoleAdmin)


class MenuAdmin(admin.ModelAdmin):
    list_display = ['name', 'pid', 'icon', 'path', 'is_frame', 'is_show', 'sort', 'component']
    pass


admin.site.register(Menu, MenuAdmin)


class PermissionAdmin(admin.ModelAdmin):
    list_display = ['name', 'pid', 'method']


admin.site.register(Permission, PermissionAdmin)