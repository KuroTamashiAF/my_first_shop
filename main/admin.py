from django.contrib import admin
from main.models import FeedBackCall

# Register your models here.

@admin.register(FeedBackCall)
class FeedBackCallAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "phone_number","time_created"]
    list_display_links=["name"]
    search_fields=["name", "phone_number"]