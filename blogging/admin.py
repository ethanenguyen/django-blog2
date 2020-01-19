from django.contrib import admin
from blogging.models import Post, Category


admin.site.register(Post)
admin.site.register(Category)


class PostInline(admin.TabularInline):
    model = Post
    # exclude = ('posts',)

class CategoryAdmin(admin.ModelAdmin):
    inlines = [
        PostInline,
    ]

    exclude = ('posts',)