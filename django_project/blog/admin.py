from django.contrib import admin
from .models import Post
from .models import Game

class GameAdmin(admin.ModelAdmin):
    list_display = ("title", "description", "genres", "tags", "developers", "publishers", 
    "platforms", "places_to_purchase",   "rec_1", "rec_2", "rec_3", "rec_4", "rec_5")

admin.site.register(Post)
admin.site.register(Game)
