from django.contrib import admin

# Register your models here.
from rbac.models import *


class UserProfileAdmin(admin.ModelAdmin):
    pass


admin.site.register(UserProfile, UserProfileAdmin)
