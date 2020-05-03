from django.contrib import admin
from .models import Post
from .models import Game

class GameAdmin(admin.ModelAdmin):
    list_display = ("title", "recommendations",)

admin.site.register(Post)
admin.site.register(Game)
