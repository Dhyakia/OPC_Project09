from django.contrib import admin

from authentication.models import User


class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'is_staff', 'is_active')


admin.site.register(User, UserAdmin)
