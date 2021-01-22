from django.contrib import admin

from portfolio.models import Portfolio, Category, Post, Contact


class PortfolioAdmin(admin.ModelAdmin):
    fields = ['title', 'home_description']
    list_display = ['title', 'home_description']


class CategoryAdmin(admin.ModelAdmin):
    fields = ['name']
    list_display = ['name']

class PostAdmin(admin.ModelAdmin):
    fields = ['title', 'short_description', 'post_text', 'use_in_home_screen', 'category']
    list_display = ['title', 'short_description', 'post_text', 'use_in_home_screen', 'category']

class ContactAdmin(admin.ModelAdmin):
    fields = ['portfolio', 'contact_text']
    list_display = ['portfolio', 'contact_text']

admin.site.register(Portfolio, PortfolioAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Contact, ContactAdmin)
