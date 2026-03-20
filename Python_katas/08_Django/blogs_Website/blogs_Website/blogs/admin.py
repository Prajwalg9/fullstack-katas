from django.contrib import admin
from .models import Author, Comment, Tag, Blog

class PostAdmin(admin.ModelAdmin):
    list_display = ('title','description', 'author', 'image', 'date', 'category')
    list_filter = ('author', 'date', 'category')


class CommentsAdmin(admin.ModelAdmin):
    list_display = ('user_name', 'user_email', 'blog','text')
    list_filter = ('blog',)
    
    
# Register your models here.


admin.site.register(Author)
admin.site.register(Tag)
admin.site.register(Blog, PostAdmin)
admin.site.register(Comment,CommentsAdmin)