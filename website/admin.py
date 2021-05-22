from django.contrib import admin

from website.models import Authors, Category, Tag, Post

admin.site.register(Authors)
admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Post)
