from django.contrib import admin

from .models import Post
# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ['title_post', 'pub_date_post']
    list_filter = ['pub_date_post']
    search_fields = ['id']
admin.site.register(Post, PostAdmin)
