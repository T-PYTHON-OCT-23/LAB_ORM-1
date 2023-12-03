from django.contrib import admin
from .models import Comment,Blogs
# Register your models here.

class BlogsAdmin(admin.ModelAdmin):
    
    list_display = ('title','catagory','is_published',)
    list_filter = ('is_published','catagory')

class CommentAdmin(admin.ModelAdmin):

    list_display = ('movie','rating','create_ar',)
    list_filter = ('rating','movie','create_ar')


admin.site.register(Blogs,BlogsAdmin)
admin.site.register(Comment,CommentAdmin)