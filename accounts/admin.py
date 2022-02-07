from django.contrib import admin

from accounts.models import Profile


class ProfileAdmin(admin.ModelAdmin):
    list_display = ['email']

admin.site.register(Profile, ProfileAdmin)