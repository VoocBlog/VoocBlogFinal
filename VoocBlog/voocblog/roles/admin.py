from django.contrib import admin

# Register your models here.
from .models import Post, Category

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['topic']
admin.site.register(Category, CategoryAdmin)

class PostAdmin(admin.ModelAdmin):
    list_display = ['title_post', 'pub_date_post']
    list_filter = ['pub_date_post']
    search_fields = ['title_post']
admin.site.register(Post, PostAdmin)


