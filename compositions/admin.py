from django.contrib import admin
from .models import Songs, UserProfile, Like, Comment


class SongsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'image', 'audio',)


admin.site.register(Songs, SongsAdmin)
admin.site.register(UserProfile)
admin.site.register(Like)
admin.site.register(Comment)
