from django.contrib import admin
from testapp.models import Post,Comment
# Register your models here.

class Post_admin(admin.ModelAdmin):
    list=['product_id','product_name','desc','pub_date']

class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'body', 'post', 'created_on', 'active')
    list_filter = ('active', 'created_on')
    search_fields = ('name', 'email', 'body')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(active=True)

    
admin.site.register(Post,Post_admin)
admin.site.register(Comment,CommentAdmin)
