from django.contrib import admin
from .models import Portfolio, PortfolioTag

# Register your models here.
class PortfolioAdmin(admin.ModelAdmin): #adds fields to list view of admin page   
    list_display = ("id", "title", "is_published", "created_date")
    list_display_links = ("id", "title") #allow link
    list_filter  = ("is_published",) #adds filter
    list_per_page = 10 # define max items per page
    list_editable = ("is_published", )
    search_fields = ("title", "description", "subtitle")

class PortfolioTagAdmin(admin.ModelAdmin):
    list_editable = ("portfolio_tag",)
    search_fields = ("portfolio_tag",)
    list_display = ("id", "portfolio_tag",)


admin.site.register(Portfolio, PortfolioAdmin)
admin.site.register(PortfolioTag, PortfolioTagAdmin)