from django.contrib import admin
from .models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'post_title', 'post_auther', 'published_date']
    list_display_links = ['id', 'post_title']
    ordering = ['post_title']
    list_filter = ['published_date']
    # Only accept character fields in search
    search_fields = ['post_title', 'post_auther']

# Register your models here.
#admin.site.register(Post, PostAdmin)
