# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from models import WebSite
from models import Tag

class WebSiteAdmin(admin.ModelAdmin):
    list_display = ('title', 'url', 'author')
    search_fields = ['title']

class TagAdmin(admin.ModelAdmin):
    list_display = ('name', 'author')
    search_fields = ('name',)

admin.site.register(WebSite, WebSiteAdmin)
admin.site.register(Tag, TagAdmin)
