from django.contrib import admin
from .models import Post, Comment, Tag

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'post_title', 'post_auther', 'published_date']
    list_display_links = ['id', 'post_title']
    ordering = ['post_title']
    list_filter = ['published_date']
    # Only accept character fields in search
    search_fields = ['post_title', 'post_auther']

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['id', 'comment_author', 'comment_date', 'post']
    list_display_links = ['id', 'comment_author']
    ordering = ['comment_date']
    list_filter = ['comment_date']
    search_fields = ['comment_author__username', 'comment_content']      

    def short_content(self, obj):
        return obj.comment_content[:30]
    
@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    list_display_links = ['id', 'name']
    ordering = ['name']
    search_fields = ['name']    

# Register your models here.
#admin.site.register(Post, PostAdmin)
#admin.site.register(Comment, CommentAdmin)
#admin.site.register(Tag, TagAdmin)
