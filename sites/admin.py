# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from models import WebSite

class WebSiteAdmin(admin.ModelAdmin):
    list_display = ('title', 'url', 'author')
    search_fields = ['title']

admin.site.register(WebSite, WebSiteAdmin)
