from django.contrib import admin
from .models import Blog_post, Blog_Image

# Register your models here.
    
class Blog_ImageInline(admin.TabularInline):
    model = Blog_Image
    extra = 1
    
class Blog_postAdmin(admin.ModelAdmin): #adds fields to list view of admin page   
    list_display = ("id", "title", "is_published", "created_date", "author")
    list_display_links = ("id", "title") #allow link
    list_filter  = ("author","is_published") #adds filter
    list_per_page = 25 # define max items per page
    list_editable = ("is_published", )
    search_fields = ("title", "body", "subtitle")
    inlines = [
        Blog_ImageInline,
    ]


admin.site.register(Blog_post, Blog_postAdmin)