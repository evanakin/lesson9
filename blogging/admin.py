from django.contrib import admin

from blogging.models import Post, Category


class CategoryInline(admin.TabularInline):
    model = Post.categories.through


class PostAdmin(admin.ModelAdmin):
    inlines = [
        CategoryInline,
    ]


class CategoryAdmin(admin.ModelAdmin):
    exclude = ("posts",)


admin.site.register(Post)
admin.site.register(Category, CategoryAdmin)
