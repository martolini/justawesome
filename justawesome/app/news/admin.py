from django.contrib import admin
from .models import Provider, Article, Author, League

admin.site.register(Article)
admin.site.register(Author)
admin.site.register(League)
admin.site.register(Provider)
