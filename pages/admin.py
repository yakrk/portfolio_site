from django.contrib import admin
from .models import Portfolio, Tag

# Register your models here.
class PortfolioAdmin(admin.ModelAdmin): #adds fields to list view of admin page   
    list_display = ("id", "title", "is_published", "created_date")
    list_display_links = ("id", "title") #allow link
    list_filter  = ("is_published",) #adds filter
    list_per_page = 10 # define max items per page
    list_editable = ("is_published", )
    search_fields = ("title", "description", "subtitle")

class TagAdmin(admin.ModelAdmin):
    list_editable = ("tag",)
    search_fields = ("tag",)
    list_display_links = ("tag",)
    list_display = ("tag",)


admin.site.register(Portfolio, PortfolioAdmin)
admin.site.register(Tag)