from django.contrib import admin

from follower.models import Follower

class FollowerAdmin(admin.ModelAdmin):
    pass

admin.site.register(Follower, FollowerAdmin)